import configparser
import requests
import os.path
import os
import time
import json
import click
import IPython.display
from itertools import islice

from .utils import line_search_return
from .walkup import *
from .dsl_grammar import G



USER_DIR = os.path.expanduser("~/.dimensions/")
USER_CONFIG_FILE_NAME = "dsl.ini"
USER_CONFIG_FILE_PATH = os.path.expanduser(USER_DIR + USER_CONFIG_FILE_NAME)
USER_JSON_OUTPUTS_DIR = os.path.expanduser(USER_DIR + "json/")
USER_HISTORY_FILE = os.path.expanduser(USER_DIR + "history.txt")


def _get_init_file():
    """
    LOGIC

    a) if dsl.ini credentials file in WD that overrides everything
    b) try user level credentials ("~/.dimensions/") 
    c) try navigating up directory tree for dsl.ini

    => a) and c) are useful for jup notebooks without system wide installation
    => b) is the usual case for CLI

    ===================
    BACKGROUND 

    Authentication details can be stored in a `dsl.ini` file
    File contents need to have this structure:

    [instance.live]
    url=https://app.dimensions.ai
    login=your_username
    password=your_password

    The section name has to start with "instance."
    Keyword "live" is the default name for most installations.

    If you have access to other Dimensions APIs just add an entry for them with a suitable name.
    ===================
    """
    if os.path.exists(os.getcwd() + "/" + USER_CONFIG_FILE_NAME):
        return os.getcwd() + "/" + USER_CONFIG_FILE_NAME
    elif os.path.exists(os.path.expanduser(USER_CONFIG_FILE_PATH )):
        return os.path.expanduser(USER_CONFIG_FILE_PATH )
    else:
        for c,d,f in walk_up(os.getcwd()):
            if os.path.exists(c + "/" + USER_CONFIG_FILE_NAME):
                return c + "/" + USER_CONFIG_FILE_NAME
    return None

def _get_file_contents(fpath, instance_name):
    """
    parse the credentials file
    """
    config = configparser.ConfigParser()
    try:
        config.read(fpath)
    except:
        click.secho(f"ERROR: `{USER_CONFIG_FILE_NAME}` credentials file not found." , fg="red")
        click.secho("HowTo: https://github.com/lambdamusic/dimcli#credentials-file", fg="red")
        raise
    # we have a good config file
    try:
        section = config['instance.' + instance_name]
    except:
        click.secho(f"ERROR: Credentials file `{fpath}` does contain settings for instance: {instance_name}", fg="red")
        click.secho("HowTo: https://github.com/lambdamusic/dimcli#credentials-file", fg="red")
        raise
    return section



class Dsl():
    """
    Object for abstracting common interaction steps with the Dimensions API. 
    Most often you just want to instantiate, autheticate and query() - yeah!

    >>> import dimcli
    >>> dsl = dimcli.Dsl()
    # if you have set up a credentials file, no need to pass log in details
    >>> dsl = dimcli.Dsl(user="me@mail.com", password="secret")
    # queries always return a Result object (subclassing IPython.display.JSON)
    >>> dsl.query("search grants for \"malaria\" return researchers")
    >>> <dimcli.dimensions.Result object>
    # use the .data method to get the JSON
    >>> dsl.query("search grants for \"malaria\" return researchers").data
    >>> {'researchers': [{'id': 'ur.01332073522.49',
            'count': 75,
            'last_name': 'White',
            'first_name': 'Nicholas J'},
        "... JSON data continues ... "

    """
    def __init__(self, instance="live", user="", password="", endpoint="https://app.dimensions.ai", show_results=False):
        # print(os.getcwd())
        if user and password:
            self._url = endpoint
            self._username = user
            self._password = password
        else:
            fpath = _get_init_file()
            config_section = _get_file_contents(fpath, instance)
            self._url = config_section['url']
            self._username = config_section['login']
            self._password = config_section['password']

        self._show_results = show_results
        self._login()

    def _login(self):
        login = {'username': self._username, 'password': self._password}
        response = requests.post(
            '{}/api/auth.json'.format(self._url), json=login)
        response.raise_for_status()

        token = response.json()['token']
        self._headers = {'Authorization': "JWT " + token}

    def query(self, q, show_results=None, retry=0):
        """
        Execute a DSL query.
        By default it doesn't show results, but it uses the iPython rich widgets for it, optimized for Jupyter Notebooks.
        """
        #   Execute DSL query.
        response = requests.post(
            '{}/api/dsl.json'.format(self._url), data=q, headers=self._headers)
        if response.status_code == 429:  
            # Too Many Requests
            print(
                'Too Many Requests for the Server. Sleeping for 30 seconds and then retrying.'
            )
            time.sleep(30)
            return self.query(q)
        elif response.status_code == 403:  
            # Forbidden:
            print('Login token expired. Logging in again.')
            self._login()
            return self.query(q)
        elif response.status_code in [200, 400, 500]:  
            ###  
            # OK or Error Info :-)
            ###
            try:
                res_json = response.json()
            except:
                print('Unexpected error. JSON could not be parsed.')
                return response
            result = Result(res_json)
            if show_results or (show_results is None and self._show_results):
                IPython.display.display(result)
            return result
        else:
            if retry > 0:
                print('Retrying in 30 secs')
                time.sleep(30)
                return self.query(
                    q,
                    retry=retry - 1)
            else:
                response.raise_for_status()



    def query_iterative(self, q, show_results=None, skip=0, limit=1000):
        """
        Runs a normal query iteratively, by automatically turning it into a loop with limit/skip operators until all the results available have been extracted. 
        """
        # @TODO is there a hard limit of 50k results for limit/skip?
        if q.split().count('return') != 1:
            raise Exception("Loop queries support only 1 return statement")
        if "limit" in q or "skip" in q:
            raise Exception("Loop queries should not contain the keywords `limit` or `skip`")
        sourcetype = line_search_return(q)  
        if not (sourcetype in G.sources()):
            raise Exception("Loop queries can return only one of the Dimensions sources: %s" % ", ".join([s for s in G.sources()])) 
        
        output = []
        q2 = q + " limit %d skip %d" % (limit, skip)
        
        res = self.query(q2, show_results=False, retry=0)

        if res['errors']:
            return res
        elif res['stats']:

            tot = int(res['stats']['total_count'])
            batch = skip+limit
            if batch > tot:
                batch = tot
            print("%d / %d" % (batch, tot  ))

            if len(res[sourcetype]) == limit:
                output = res[sourcetype] + self.query_iterative(q, show_results, skip+limit)
            else:
                output = res[sourcetype]

            # FINALLY 
            #
            # if recursion is complete (we are at top level, hence skip=0) 
            #   build the Result obj
            # else 
            #   just return current iteration results 
            #
            if skip == 0: 
                response_simulation = {
                    "_stats": {
                        "total_count": tot
                        },
                    sourcetype: output
                }
                result = Result(response_simulation)
                if show_results or (show_results is None and self._show_results):
                    IPython.display.display(result)
                return result
            else:
                return output






class Result(IPython.display.JSON):
    """
    Wrapper for JSON results from DSL

    >>> res = dsl.query("search publications return publications")
    >>> res.data # => shows the underlying JSON data
    >>> res.json # => same 

    # Magic methods: 

    >>> res['publications'] # => the dict section
    >>> res.['xxx'] # => false, not found
    >>> res.['stats'] # => the _stats dict

    """
    def __init__(self, data):
        IPython.display.JSON.__init__(self, data)
        self.json = self.data
        for k in self.json.keys(): # add result dict keys as attributes dynamically
            if k == "_stats":
                setattr(self, "stats", self.json[k])
            else:
                setattr(self, k, self.json[k])

    def __getitem__(self, key):
        "return dict key as slice"
        if key == "stats":
            key = "_stats" # syntactic sugar
        if key in self.json:
            return self.json[key]
        else:
            return [] # empty list so to support iteration tests / previously: False

    def __len__(self):
        "Return length of first object in JSON (skipping '_stats'"
        k = self._good_data_keys()
        try:
            return len(self.json[k[0]])
        except:
            return 0

    def _good_data_keys(self,):
        "return the results keys other than stats"
        skips = ["_warnings", "_stats"]
        return [x for x in self.json.keys() if x not in skips]

    def keys_and_count(self,):
        "Utility to preview contents of results object"
        return [(x, len(self.json[x])) for x in self.json.keys()]

    def as_dataframe(self, key=""):
        "utility method: return inner json as a pandas dataframe"
        try:
            import pandas as pd
        except:
            print("Sorry this functionality requires the Pandas python library. Please install it first.")
            return
            
        if not key:
            if len(self._good_data_keys()) > 1:
                print(f"Please specify a key from {self._good_data_keys()}")
                return
            else:
                key = self._good_data_keys()[0]
        elif key not in self._good_data_keys():
            print(f"Invalid key: should be one of {self._good_data_keys()}")
            return 

        return pd.DataFrame().from_dict(self.json[key])


    def chunks(self, key="", size=400, ):
        """
        Return an iterator for going through chunks of the JSON results. 
        NB the first available dict key is taken, to determine what is the data 
        object being returned. 
        Default size of chunks = 400 elements

        EG

        res = dslquery("search publications return publications limit 1000")
        test = [len(x) for x in res.chunks()]

        """

        if not key:
            if len(self._good_data_keys()) > 1:
                print(f"Please specify a key from {self._good_data_keys()}")
                return
            else:
                key = self._good_data_keys()[0]
        elif key not in self._good_data_keys():
            print(f"Invalid key: should be one of {self._good_data_keys()}")
            return 

        it = iter(self.json[key])
        chunk = list(islice(it, size))
        while chunk:
            yield chunk
            chunk = list(islice(it, size))


    def __repr__(self):
        return "<dimcli.Result object #%s. Dict keys: %s>" % (str(id(self)), ", ".join([f"'{x}'" for x in self.json]))



