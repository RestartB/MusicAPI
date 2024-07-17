# MusicAPI
Music player, controlled by an API

## API Documentation
### /active *(GET)*
Returns a blank JSON response ASAP when then API is running.

#### Example Response
```json
{}
```

#### Errors
- No Response - API is not active

###  /about *(GET)*
Get info about the API.

#### Example Response
```json
{
    "version": "dev",
    "github": "https://github.com/RestartB/MusicAPI"
}
```

#### Errors
N/A

### /playlists *(GET)*
Get a list of playlists. A list of songs in each playlist is not returned, run /playlist for this information.

#### Example Response
```json
{
    "amount": 2,
    "playlists": [
        {
            "name": "Playlist 1",
            "description": "This is a playlist!",
            "id": "1",
            "hasCoverImage": true,
            "items": {
                "amount": 0,
                "href": "http://172.0.0.1/playlist?id=1"
            }
        },
        {
            "name": "Playlist 2",
            "description": "This is another playlist!",
            "id": "2",
            "hasCoverImage": false,
            "items": {
                "amount": 0,
                "href": "http://172.0.0.1/playlist?id=2"
            }
        },
    ]
}
```