from dotenv import load_dotenv;
import os;
from urllib.parse import urlencode
import base64;
import requests;
import json;
from requests import post,get;
load_dotenv();




clientId=os.getenv("CLIENT_ID");
clientSecret=os.getenv("CLIENT_SECRET");
playlistId=os.getenv("PLAYLISTID");
redirect_uri=os.getenv("redirect_uri");

def getAuthToken(token):
    return {"Authorization": "Bearer " + token};

def get_authorization_url():
    # Step 1: Generate the authorization URL
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": clientId,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "playlist-modify-public playlist-modify-private playlist-read-private"  # Add necessary scopes
    }
    return f"{auth_url}?{urlencode(params)}"


def exchange_code_for_tokens(code):
    # Step 2: Exchange authorization code for access and refresh tokens
    token_url = "https://accounts.spotify.com/api/token"
    auth_string = f"{clientId}:{clientSecret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
    }

    response = requests.post(token_url, headers=headers, data=data)
    response_data = json.loads(response.text)
    return response_data["access_token"]
    # You can now use response_data["access_token"] to make authorized API requests.

def getUserPlayList(token):
    playList=[];
    url="https://api.spotify.com/v1/me/playlists";
    headers=getAuthToken(token);
    result=requests.get(url,headers=headers);
    response=json.loads(result.content);
    if result.status_code == 200:
        print("successfull!")
    else:
        print(f"Failed. Status Code: {response.status_code}")
    for ind,item in enumerate(response["items"]):
        playList.append({"ind":ind+1,"Name":item["name"],"id":item["id"]})
       
    return playList;


def getPlayListTrack(token,playlistId):
    url = f"https://api.spotify.com/v1/playlists/{playlistId}/tracks"
    headers=getAuthToken(token);
    all_tracks = []  # Create a list to store all tracks

    # Initialize offset and limit
    offset = 0
    limit = 100  # Maximum limit per request

    while True:
        # Make the API request with offset and limit
        params = {"offset": offset, "limit": limit}
        result = get(url, headers=headers, params=params)

        if result.status_code == 200:
            jsonResult = json.loads(result.content)
            tracks = jsonResult.get("items", [])

            # Append the retrieved tracks to the list
            all_tracks.extend(tracks)

            # If there are more tracks to fetch, update the offset
            if len(tracks) < limit:
                break
            else:
                offset += limit
    trackList=[];            
    for name in all_tracks:
        trackList.append({"name":name["track"]["name"],"id":name["track"]["id"],"artist":name["track"]["artists"][0]["name"]});
    return trackList;
    


def ArtistSearch(token,ArtistName):
    url="https://api.spotify.com/v1/search";
    headers=getAuthToken(token);
    query=f"?q={ArtistName}&type=artist&limit=1";

    queryResult=url+query;
    result=get(queryResult,headers=headers);
    jsonResult=json.loads(result.content)["artists"]["items"];
    if len(jsonResult)==0:
        print("No Artist Found....");
        return None;
    
    ArtistInfo={"id":jsonResult[0]["id"],"name":jsonResult[0]["name"]};
    return ArtistInfo;


def ArtistSongTop10(token,ID):
    url=f"https://api.spotify.com/v1/artists/{ID}/top-tracks?country=IN";
    headers=getAuthToken(token);
    result=get(url,headers=headers);
    jsonResult=json.loads(result.content)["tracks"];
    tenTracks=[];
    for song in jsonResult:
        tenTracks.append({"id":song["id"],"name":song["name"]});
    return tenTracks;



def addTrack(token,playListId,trackId):
    url = f"https://api.spotify.com/v1/playlists/{playListId}/tracks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "uris": [f"spotify:track:{trackId}"],
        "position": 0
    }

    response = post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Track added successfully!")
    else:
        print(f"Failed to add track. Status Code: {response.status_code}")