#! /usr/local/bin python3
import yaml
import pandas as pd
import requests
from getpass import getpass
from datetime import datetime, timedelta
import zipfile
import io

class QualtricsAPI:

  def __init__(self, config_file_or_dict):
    self.config = self.APIConfig(config_file_or_dict)

  class APIConfig:

    def __init__(self, config_file_or_dict):
      if type(config_file_or_dict) == dict:
        cfg = config_file_or_dict
      else:
        with open(config_file_or_dict, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, yaml.FullLoader)
      if 'api_token' in cfg:
        self.api_token = cfg['api_token']
      else:
        self.api_token = getpass('Enter your API token: ')

      self.data_center = cfg['data_center']
      self.default_survey_owner = cfg['default_survey_owner']
      self.default_library_owner = cfg['default_library_owner']

  def make_post_request(self, base_url: str, payload: dict, headers: dict, verbose=False):
    response = requests.post(base_url, json=payload, headers=headers)
    if verbose == True:
      print("Sending request:")
      print(response.request.body)
      print(response.request.headers)

    if response.json()['meta']['httpStatus'] != '200 - OK':
      if verbose == True:
        print('\nError response:')
        print(response.json())
      return((False, response))
    else:
      if verbose == True:
        print("\nSuccess:")
        print(response.json())
      return((True, response))

  def make_put_request(self, base_url: str, payload: dict, headers: dict, verbose=False):
    response = requests.put(base_url, json=payload, headers=headers)
    if verbose == True:
      print("Sending request:")
      print(response.request.body)
      print(response.request.headers)
    
    if response.json()['meta']['httpStatus'] == '200 - OK':
      return(True)
    else:
      if verbose == True:
        print('Request failed')
        print(response.json())
      return(False)

  def make_get_request(self, base_url: str, headers: dict, verbose=False):

    response = requests.get(base_url, headers=headers)
    if verbose == True:
      print("Sending request:")
      print("URL: {}".format(base_url))
      print("Body: {}".format(response.request.body))
      print("Headers: {}".format(response.request.headers))
    
    if verbose == True:
      print("Response : {}".format(response))
    if response.json()['meta']['httpStatus'] == '200 - OK':
      if verbose == True:
        print("\n\nSuccess:")
        print(response.json())
      return((True, response))
    else:
      if verbose == True:
        print(response.json())
      return((False, response))

  def make_delete_request(self, base_url: str, headers: dict, verbose=False):
    response = requests.delete(base_url, headers=headers)
    if verbose == True:
      print("Sending request:")
      print(response.request.body)
      print(response.request.headers)
    if response.json()['meta']['httpStatus'] == '200 - OK':
      return(True)
    else:
      if verbose == True:
        print('Request failed')
        print(response.json())
      return(False)

  def get_survey(self, survey_id, verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/surveys/{1}".format(self.config.data_center,
                                                                     survey_id)
    headers = {"x-api-token": self.config.api_token}
    (success, response) = self.make_get_request(base_url, headers, verbose)
    if success == True:
      survey = response.json()["result"]
      if verbose:
        print('\nRetrieved survey: {}'.format(survey))
      return(survey)
    else:
      if verbose:
        print(response.json())
      return()  

  def copy_survey(self, survey_id: str, new_name: str, owner=None, verbose=False):
    if owner == None:
      owner = self.config.default_survey_owner
    base_url = "https://{0}.qualtrics.com/API/v3/surveys".format(self.config.data_center)
    headers = {"CONTENT-TYPE": "application/json",
               "X-API-TOKEN": self.config.api_token,
               "X-COPY-SOURCE": survey_id,
               "X-COPY-DESTINATION-OWNER": owner
              }
    payload = {"projectName": new_name}
    (success, response) = self.make_post_request(base_url, payload, headers, verbose)
    if success == True:
      new_survey_id = response.json()["result"]["id"]
      if verbose:
        print('\nNew survey id is: {}'.format(new_survey_id))
      return(new_survey_id)
    else:
      return()

  def delete_survey(self, survey_id: str, verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/surveys/{1}".format(self.config.data_center, survey_id)
    headers = {"X-API-TOKEN": self.config.api_token}
    success = self.make_delete_request(base_url, headers, verbose)
    if success == True and verbose == True:
      print('Survey successfully deleted')
    return(success)

  def activate_survey(self, survey_id: str, 
                      start_date=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                      end_date=(datetime.utcnow() + timedelta(days=130)).strftime("%Y-%m-%dT%H:%M:%SZ"), 
                      verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/surveys/{1}".format(self.config.data_center, survey_id)
    headers = {"CONTENT-TYPE": "application/json",
               "X-API-TOKEN": self.config.api_token}
    payload = {"isActive": True,
               "expiration": {
                    "startDate": start_date, 
                    "endDate": end_date}}
    success = self.make_put_request(base_url, payload, headers, verbose)
    if success == True and verbose == True:
      print('Survey successfully activated')
    return(success)

  def create_mailing_list(self, list_name, records_to_add=pd.DataFrame(), list_category=None, 
                          owner=None, verbose=False):
    payload = {"name": list_name}
    if owner == None:
      payload["libraryId"] = self.config.default_library_owner
    else:
      payload["libraryId"] = owner
    if list_category != None:
      payload['category'] = list_category

    base_url = "https://{0}.qualtrics.com/API/v3/mailinglists".format(self.config.data_center)
    headers = {"CONTENT-TYPE": "application/json",
               "X-API-TOKEN": self.config.api_token}

    (success, response) = self.make_post_request(base_url, payload, headers, verbose)

    if success == True:
      new_ml_id = response.json()["result"]["id"]
      if verbose == True:
        print('\nNew mailing list id is: {}'.format(new_ml_id))
      if not records_to_add.empty:
        self.add_records_to_mailing_list(new_ml_id, records_to_add, verbose)
      return(new_ml_id)
    else:
      return()

  def get_mailing_list(self, ml_id, verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/mailinglists/{1}".format(self.config.data_center,
                                                                          ml_id)
    headers = {"x-api-token": self.config.api_token}
    (success, response) = self.make_get_request(base_url, headers, verbose)
    if success == True:
      ml = response.json()["result"]
      if verbose:
        print('\nRetrieved mailing list: {}'.format(ml))
      return(ml)
    else:
      if verbose:
        print(response.json())
      return()  

  def delete_mailing_list(self, list_id, verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/mailinglists/{1}".format(self.config.data_center, list_id)
    headers = {"X-API-TOKEN": self.config.api_token}
    success = self.make_delete_request(base_url, headers, verbose)
    if success == True and verbose == True:
      print('Mailing list successfully deleted')
    return(success)    

  def add_records_to_mailing_list(self, mailing_list_id: str, records_to_add: pd.DataFrame, verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/mailinglists/{1}/contacts".format(
                 self.config.data_center, mailing_list_id)
    headers = {"CONTENT-TYPE": "application/json", "X-API-TOKEN": self.config.api_token}
    
    # so that panel columns don't need to be case sensitive
    records_cp = records_to_add.copy(deep=True)
    records_cp.columns = [x.lower() for x in records_cp.columns]


    for i, row in records_cp.iterrows():
      p = {}
      try:
        p['email'] = row['email']
      except Exception(e):
        raise('"email" is a required field for every mailing list')
      for fn, qual_fn in [['firstname', 'firstName'], ['lastname', 'lastName'], 
                          ['externaldataref', 'externalDataRef'],
                          ['unsubscribed', 'unsubscribed'],
                          ['language', 'language']]:
        if fn in row.index:
          p[qual_fn] = row.loc[fn]
      
      if not 'unsubscribed' in p:
        p['unsubscribed'] = False
      if not 'language' in p:
        p['language'] = 'en'
      # add optional fields/embedded data
      cols_to_keep = list(filter(lambda x: x.lower() not in ['email', 
                                                             'firstname',
                                                             'lastname',
                                                             'externaldataref',
                                                             'unsubscribed',
                                                             'language'], list(records_to_add.columns)))
      
      if len(cols_to_keep) > 0:
        ed ={}
        for c in cols_to_keep:
          if pd.notnull(records_to_add.loc[i, c]):
            ed[c] = str(records_to_add.loc[i, c])
        p["embeddedData"] = ed

      (success, response) = self.make_post_request(base_url, p, headers, verbose)

      if success == True:
        if verbose == True:
          print('Successfully added {} to mailing list'.format(row['email']))
      else:
        if verbose == True:
          print('Failed to add {} to mailing list\n'.format(row['email']))
    return()

  def list_links_for_distribution(self, distribution_id, survey_id, verbose=False):
    headers = {"X-API-TOKEN": self.config.api_token}
    url = 'https://{0}.qualtrics.com/API/v3/distributions/{1}/links?surveyId={2}'.format(self.config.data_center, 
                                                                                         distribution_id,
                                                                                         survey_id)
    all_success = True
    links = []
    while url is not None:
      (success, response) = self.make_get_request(url, headers, verbose)

      if success == False:
        all_success = False
        url = None
      else:
        url = response.json()['result']['nextPage']
        links += response.json()['result']['elements']


    if all_success == True:
      if verbose:
        print('Links retrieved')
    else:
      if verbose:
        print(response.json())
      return(None)
    
    links_df = pd.DataFrame(links)
    return(links_df)

  def get_links_for_mailing_list(self, survey_id: str, mailing_list_id: str, days_to_expiry=130,
                                 description="Survey distribution", link_type='Individual',
                                 verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/distributions".format(self.config.data_center)
    headers = {"CONTENT-TYPE": "application/json", "X-API-TOKEN": self.config.api_token}
    expire_date = datetime.now() + timedelta(days=days_to_expiry)
    link_expiration = expire_date.strftime("%Y-%m-%d %H:%M:%S")
    payload = {"action": "CreateDistribution",
               "surveyId": survey_id,
               "mailingListId": mailing_list_id,
               "description": description,
               "expirationDate": link_expiration,
               "linkType": link_type}

    (success, response) = self.make_post_request(base_url, payload, headers, verbose)
    if success == True:
      distribution_id = response.json()["result"]["id"]
      if verbose == True:
        print('\nNew distribution id is: {}'.format(distribution_id))

    else:
      return()

    return(self.list_links_for_distribution(distribution_id, survey_id, verbose))

  def create_library_message(self, description, messages: dict, category='invite',
                             owner=None, verbose=False):
    """Create a message to be stored in owner's library. Parameter 'messages' is
    a mapping from language code (e.g. 'en') to a message string. Category is one
    of: invite, inactiveSurvey, reminder, thankYou, endOfSurvey, general, validation, 
    lookAndFeel, emailSubject, or smsInvite"""
    if owner == None:
      lib_id = self.config.default_library_owner
    else:
      lib_id = owner
    p = {}
    p['description'] = description
    p['messages'] = messages
    p['category'] = category
    headers = {"CONTENT-TYPE": "application/json", "X-API-TOKEN": self.config.api_token}
    base_url = """https://{}.qualtrics.com/API/v3/libraries/{}/messages""".format(self.config.data_center,
                                                                                  lib_id)
    (success, response) = self.make_post_request(base_url, p, headers, verbose)
    if success == True:
      msg_id = response.json()["result"]["id"]
      if verbose:
        print('\nNew message id is: {}'.format(msg_id))
      return(msg_id)
    else:
      return()

  def send_survey(self, 
                  survey_id,
                  message_id,
                  mailing_list_id,
                  from_email,
                  from_name,
                  subject,
                  message_library_id=None,
                  reply_to_email=None,
                  link_type='Individual',
                  send_time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                  expiration_time=(datetime.utcnow() + timedelta(days=130)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                  verbose=False):
    headers = {"CONTENT-TYPE": "application/json", "X-API-TOKEN": self.config.api_token}
    base_url = """https://{}.qualtrics.com/API/v3/distributions""".format(self.config.data_center)

    if reply_to_email == None:
      reply_to_email = from_email
    if message_library_id == None:
      message_library_id = self.config.default_library_owner
    
    sl = {'surveyId': survey_id, 'expirationDate': expiration_time, 'type': link_type}
    h = {'fromEmail': from_email, 'fromName': from_name, 'replyToEmail': reply_to_email, 'subject': subject}
    m = {'libraryId': message_library_id, 'messageId': message_id}
    r = {'mailingListId': mailing_list_id}
    p = {'surveyLink': sl, 'header': h, 'message': m, 'recipients': r, 'sendDate': send_time}

    (success, response) = self.make_post_request(base_url, p, headers, verbose)
    if success == True:
      dist_id = response.json()["result"]["id"]
      if verbose:
        print('\nNew distribution id is: {}'.format(dist_id))
      return(dist_id)
    else:
      return()

  def send_reminder(self,
                    parent_distribution_id,
                    message_id,
                    from_email,
                    from_name,
                    subject,
                    message_library_id=None,
                    reply_to_email=None,
                    send_time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    verbose=False):
    headers = {"CONTENT-TYPE": "application/json", "X-API-TOKEN": self.config.api_token}
    base_url = """https://{}.qualtrics.com/API/v3/distributions/{}/reminders""".format(self.config.data_center,
                                                                                       parent_distribution_id)
    if reply_to_email == None:
      reply_to_email = from_email
    if message_library_id == None:
      message_library_id = self.config.default_library_owner

    h = {'fromEmail': from_email, 'fromName': from_name, 'replyToEmail': reply_to_email, 'subject': subject}
    m = {'libraryId': message_library_id, 'messageId': message_id}
    p = {'header': h, 'message': m, 'sendDate': send_time}

    (success, response) = self.make_post_request(base_url, p, headers, verbose)
    if success == True:
      dist_id = response.json()["result"]["distributionId"]
      if verbose:
        print('\nNew distribution id is: {}'.format(dist_id))
      return(dist_id)
    else:
      return()

  def create_user(self,
                  username, 
                  password, 
                  first_name, 
                  last_name,
                  user_type,
                  email,
                  division_id=None,
                  account_expiration_date=None,
                  language='en',
                  verbose=False):
    base_url = """https://{}.qualtrics.com/API/v3/users""".format(
      self.config.data_center)
    headers = {
    "x-api-token": self.config.api_token,
    "Content-Type": "application/json"
    }
    data = {"username": username,
            "password": password,
            "firstName": first_name,
            "lastName": last_name,
            "userType": user_type,
            "email": email,
            "language": language}

    if division_id != None:
      data['divisionId'] = division_id
    if account_expiration_date != None:
      data['accountExpirationDate'] = account_expiration_date

    (success, response) = self.make_post_request(base_url, data, headers, verbose)
    if success == True:
      user_id = response.json()["result"]["id"]
      if verbose:
        print('\nNew user id is: {}'.format(user_id))
      return(user_id)
    else:
      return()

  def list_users(self, verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/users".format(self.config.data_center)
    headers = {"x-api-token": self.config.api_token}
    all_success = True
    users = []
    while base_url is not None:
      (success, response) = self.make_get_request(base_url, headers, verbose)
      base_url = response.json()['result']['nextPage']
      users += response.json()['result']['elements']
      if success == False:
        all_success = False


    if all_success == True:
      if verbose:
        print('Users retrieved')
      return(users)
    else:
      if verbose:
        print(response.json())
      return()

  def get_user(self, user_id, verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/users/{1}".format(self.config.data_center,
                                                                  user_id)
    headers = {"x-api-token": self.config.api_token}
    (success, response) = self.make_get_request(base_url, headers, verbose)
    if success == True:
      user = response.json()["result"]
      if verbose:
        print('\nRetrieved user: {}'.format(user))
      return(user)
    else:
      if verbose:
        print(response.json())
      return()   

  def update_user(self,
                  user_id,
                  username=None,  
                  first_name=None, 
                  last_name=None,
                  user_type=None,
                  division_id=None,
                  status=None,
                  language='en',
                  time_zone=None,
                  permissions=None,
                  account_expiration_date=None,
                  verbose=False):
    base_url = "https://{0}.qualtrics.com/API/v3/users/{1}".format(self.config.data_center,
                                                                  user_id)
    headers = {"x-api-token": self.config.api_token}
    data = {}
    if username != None:
      data['username'] = username
    if first_name != None:
      data['firstName'] = first_name
    if last_name != None:
      data['lastName'] = last_name   
    if user_type != None:
      data['userType'] = user_type
    if division_id != None:
      data['divisionId'] = division_id
    if status != None:
      data['status'] = status
    if language != None:
      data['language'] = language
    if time_zone != None:
      data['timeZone'] = time_zone
    if permissions != None:
      data['permissions'] = permissions
    if account_expiration_date != None:
      data['accountExpirationDate'] = account_expiration_date
    success = self.make_put_request(base_url, data, headers, verbose)
  
    if verbose == True:
      if success == True:
        print('Survey successfully updated')
      else:
        print('User not successfully updated')
    
    return(success)

  def create_response_export(self, 
                             survey_id,
                             format,
                             start_date=None,
                             end_date=None,
                             limit=None,
                             use_labels=None,
                             seen_unanswered_recode=None,
                             multiselect_seen_unanswered_recode=None,
                             include_display_order=None,
                             format_decimal_as_comma=None,
                             time_zone=None,
                             newline_replacement=None,
                             question_ids=None,
                             embedded_data_ids=None,
                             survey_metadata_ids=None,
                             compress=None,
                             verbose=False):
    base_url = 'https://{}.qualtrics.com/API/v3/surveys/{}/export-responses'.format(self.config.data_center,
                                                                                    survey_id)
    headers = {"x-api-token": self.config.api_token}
    data = {"format": format}
    for var, varname in [
      [start_date, 'startDate'],
      [end_date, 'endDate'],
      [limit, 'limit'],
      [use_labels, 'useLabels'],
      [seen_unanswered_recode, 'seenUnansweredRecode'],
      [multiselect_seen_unanswered_recode, 'multiselectSeenUnansweredRecode'],
      [include_display_order, 'includeDisplayOrder'],
      [format_decimal_as_comma, 'formatDecimalAsComma'],
      [time_zone, 'timeZone'],
      [newline_replacement, 'newlineReplacement'],
      [question_ids, 'questionIds'],
      [embedded_data_ids, 'embeddedDataIds'],
      [survey_metadata_ids, 'surveyMetadataIds'],
      [compress, 'compress']]:
      if var != None:
        data[varname] = var

    (success, response) = self.make_post_request(base_url, data, headers, verbose)
    if success == True:
      progress_id = response.json()["result"]["progressId"]
      if verbose:
        print('\nProgress id is: {}'.format(progress_id))
      return(progress_id)
    else:
      if verbose:
        print('Response export not created')
      return()

  def get_response_export_progress(self, survey_id, export_progress_id, verbose=False):
    base_url = 'https://{}.qualtrics.com/API/v3/surveys/{}/export-responses/{}'.format(self.config.data_center,
                                                                                       survey_id,
                                                                                       export_progress_id)
    headers = {"x-api-token": self.config.api_token}
    (success, response) = self.make_get_request(base_url, headers, verbose)
    if success == True:
      percent_complete = response.json()["result"]["percentComplete"]
      status = response.json()["result"]["status"]
      if status == 'complete':
        file_id = response.json()["result"]["fileId"]
      else:
        file_id = None
      if verbose:
        print('\nRetrieved export progress: {}% complete, status {}, file id {}'.format(percent_complete, status, file_id))
      return((status, file_id))
    else:
      if verbose:
        print('Failed to retrieve export progress')
      return()  

  def get_response_export_file_as_dataframe(self, survey_id, file_id, verbose=False):
    base_url = 'https://{}.qualtrics.com/API/v3/surveys/{}/export-responses/{}/file'.format(self.config.data_center,
                                                                                       survey_id,
                                                                                       file_id)
    headers = {"x-api-token": self.config.api_token}
    download = requests.request("GET", base_url, headers=headers, stream=True)

    try:
      zfobj = zipfile.ZipFile(io.BytesIO(download.content))
      for name in zfobj.namelist():
        uncompressed = zfobj.read(name)
        df = pd.read_csv(io.StringIO(uncompressed.decode('utf-8')), skiprows=[1, 2])
      return(df)
    except Exception as e:
      if verbose:
        print(e)
      return()
    