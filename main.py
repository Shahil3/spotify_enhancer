from functions import*;


if __name__ == "__main__":
    # Step 1: Generate the authorization URL
    auth_url = get_authorization_url()
    print(f"Authorize your app by visiting the following URL:\n{auth_url}")

    # After the user authorizes your app, they will be redirected back with an authorization code.
    authorization_code = input("Enter the authorization code from the callback URL: ")

    # Step 2: Exchange the authorization code for access and refresh tokens
    


token=exchange_code_for_tokens(authorization_code);

playlists=getUserPlayList(token);
for playList in playlists:
    print(f"{playList['ind']}  {playList['Name']}");


playListInd=input("which playlist so you want to expand....just type its index..");
# print(playListInd)
PLayListId="";
for list1 in playlists:
    # print(list["ind"]);
    playListInd=int(playListInd);
    if(list1["ind"]==playListInd):
        # print(list["ind"]);
        # print(playListInd);
        playlistId=list1["id"];
        break;

tracks=getPlayListTrack(token,playlistId);
trackArtist=[];
for track in tracks:
    trackArtist.append(track["artist"]);

# print(trackArtist);

artistsId=[];
for artist in trackArtist:
    ArtistInfo=(ArtistSearch(token,artist));
    if(ArtistInfo==None):
        continue;
    
    artistsId.append(ArtistInfo["id"]);
# print(artistsId);
artistsId=list(set(artistsId));

# print(artistsId);

allTracks=[];
original=getPlayListTrack(token,playlistId);
for li in original:
    allTracks.append(li["id"]);

for id in artistsId:
    TenTracks=ArtistSongTop10(token,id);
    for track in TenTracks:
        allTracks.append(track["id"]);

allTracks=list(set(allTracks));
# print(allTracks);
for tr in allTracks:
    if tr not in original:
        addTrack(token,playlistId,tr);
        





