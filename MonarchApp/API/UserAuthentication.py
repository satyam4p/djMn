import requests
import configparser
import urllib.parse as urlParser
from ..models import users
from ..Utils.generateUserDataAndUpdateTable import updateUserTable
from django.db import *

cfg_parse = configparser.RawConfigParser()

def user_auth(input_json):
    # print("inside user authentication function ::: ",input_json)
    cfg_parse.read('MonarchApp/Config/active_dir_config.cfg')
    email = input_json.get('email')
    password = input_json.get('password')
    # print("email and password are:: ",email,password)
    if email.split('@')[1] == "bridgesgi.com":
        url = cfg_parse.get('ad-config', 'url')
        content_type = cfg_parse.get('ad-config', 'content-type')
        sdkVersion = cfg_parse.get('ad-config', 'SdkVersion')
        client_id = cfg_parse.get('ad-config', 'client_id')
        client_secret = cfg_parse.get('ad-config', 'client_secret')
        grant_type = cfg_parse.get('ad-config', 'grant_type')
        scope = cfg_parse.get('ad-config', 'scope')
        # print("details from cfg :: ", url)
        headers = {"Content-Type": content_type,
                   "SdkVersion": sdkVersion}
        data_values = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "scope": scope,
            "userName": email,
            "password": password
        }
        body = urlParser.urlencode(data_values)
        # print("data to be sent to request::: ", body)
        responseFromAD = requests.post(url, headers=headers, data=body)
        print("response from AD::: ", responseFromAD.status_code)
        statusCode = responseFromAD.status_code
        if statusCode == 200:
            contentFromResponse = responseFromAD.json()
            # print("content from AD:: ",contentFromResponse)
            token = contentFromResponse.get('access_token')
            # print("token:: ",token)
            expires_in = contentFromResponse.get('expires_in')
            print(expires_in)
            userExists = users.objects.all().filter(user_email=email).exists()
            print("user email exists or not::: ", userExists)
            if not userExists:
                userKey = updateUserTable(email,password)
                if userKey:
                    print("new user created")
                    output_json = {}
                    output_json.update({'user_key': userKey})
                    output_json.update({'token': token})
                    output_json.update({'status_code': statusCode})
                    return output_json
                else:
                    raise DataError
            else:
                print("user already exists")
                output_json = {}
                userKey = users.objects.get(user_email = email).user_key
                output_json.update({'user_key': userKey})
                output_json.update({'token': token})
                output_json.update({'status_code': statusCode})
                print("output_json is:: ",output_json)
                return output_json
        else:
            pass
    else:
        output_json = {"statucCode":"400",
                      "content":"invalid Credentials"}
        return output_json


















