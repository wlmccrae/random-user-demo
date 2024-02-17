from fastapi import APIRouter

from models.users import UserIn, UserOut, UsersOut

router = APIRouter()

users = [
            {
            "gender": "male",
            "name": {
                "title": "Mr",
                "first": "Jordan",
                "last": "Clark"
            },
            "location": {
                "street": {
                "number": 6139,
                "name": "W 6th St"
                },
                "city": "Townsville",
                "state": "Western Australia",
                "country": "Australia",
                "postcode": 2639,
                "coordinates": {
                "latitude": "-88.6885",
                "longitude": "-157.3142"
                },
                "timezone": {
                "offset": "-1:00",
                "description": "Azores, Cape Verde Islands"
                }
            },
            "email": "jordan.clark@example.com",
            "login": {
                "uuid": "8269dde3-84f9-4a00-8ad9-73723a4f2c00",
                "username": "ticklishmouse518",
                "password": "oranges",
                "salt": "Fq9KQbbV",
                "md5": "a8e2b4fdd8e4cb0510b26967ee485afb",
                "sha1": "e6e12f88faf71255ea563eb265015a9e88d71957",
                "sha256": "0df6c890246596e4d32d05bad9a836c3c4897a904aabe26c8b5341ebea102120"
            },
            "dob": {
                "date": "1955-09-07T12:48:19.484Z",
                "age": 68
            },
            "registered": {
                "date": "2011-12-09T07:53:03.552Z",
                "age": 11
            },
            "phone": "02-6291-8005",
            "cell": "0450-922-333",
            "id": {
                "name": "TFN",
                "value": "727753047"
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/men/12.jpg",
                "medium": "https://randomuser.me/api/portraits/med/men/12.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/men/12.jpg"
            },
            "nat": "AU"
            },
            {
            "gender": "female",
            "name": {
                "title": "Ms",
                "first": "Ilona",
                "last": "Korpela"
            },
            "location": {
                "street": {
                "number": 659,
                "name": "Satakennankatu"
                },
                "city": "Valkeakoski",
                "state": "Central Finland",
                "country": "Finland",
                "postcode": 15101,
                "coordinates": {
                "latitude": "11.3545",
                "longitude": "8.2709"
                },
                "timezone": {
                "offset": "-8:00",
                "description": "Pacific Time (US & Canada)"
                }
            },
            "email": "ilona.korpela@example.com",
            "login": {
                "uuid": "0f43655b-4cb9-4517-b35e-65f21ce00763",
                "username": "organicgoose177",
                "password": "johngalt",
                "salt": "EAp2ck4k",
                "md5": "032c291b9ea6a2d8cb18f6c94a0fb4d2",
                "sha1": "8739e70ca4cda8893dd21759c929c2fc88e1e797",
                "sha256": "d33039fe0627d3311eb9e02e8203fb6b71a757db3362ff55fe186c3dd222b69a"
            },
            "dob": {
                "date": "1957-04-06T17:58:40.412Z",
                "age": 66
            },
            "registered": {
                "date": "2014-10-26T13:08:31.387Z",
                "age": 8
            },
            "phone": "05-333-361",
            "cell": "041-655-43-05",
            "id": {
                "name": "HETU",
                "value": "NaNNA144undefined"
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/women/80.jpg",
                "medium": "https://randomuser.me/api/portraits/med/women/80.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/women/80.jpg"
            },
            "nat": "FI"
            },
            {
            "gender": "male",
            "name": {
                "title": "Mr",
                "first": "Arthur",
                "last": "White"
            },
            "location": {
                "street": {
                "number": 7652,
                "name": "Castle Street"
                },
                "city": "Hamilton",
                "state": "Gisborne",
                "country": "New Zealand",
                "postcode": 50308,
                "coordinates": {
                "latitude": "65.8010",
                "longitude": "-163.7427"
                },
                "timezone": {
                "offset": "+6:00",
                "description": "Almaty, Dhaka, Colombo"
                }
            },
            "email": "arthur.white@example.com",
            "login": {
                "uuid": "2e279513-9d76-4546-a11a-887418277c11",
                "username": "heavypanda217",
                "password": "achtung",
                "salt": "rXrIGe41",
                "md5": "4c4715889650ee79c8a106456624b854",
                "sha1": "a381bdce335d273d5d4eb4895119c5ec4d397854",
                "sha256": "0c6149553ee5beca5e5d7e283b09cdcce9d7b77157c7f331c177abe30b5ec162"
            },
            "dob": {
                "date": "1995-01-17T23:50:26.132Z",
                "age": 28
            },
            "registered": {
                "date": "2014-11-12T17:56:22.120Z",
                "age": 8
            },
            "phone": "(597)-869-1465",
            "cell": "(359)-137-6695",
            "id": {
                "name": "",
                "value": None
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/men/27.jpg",
                "medium": "https://randomuser.me/api/portraits/med/men/27.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/men/27.jpg"
            },
            "nat": "NZ"
            },
            {
            "gender": "female",
            "name": {
                "title": "Miss",
                "first": "Esma",
                "last": "Dağlaroğlu"
            },
            "location": {
                "street": {
                "number": 9452,
                "name": "Filistin Cd"
                },
                "city": "Hatay",
                "state": "Kilis",
                "country": "Turkey",
                "postcode": 91278,
                "coordinates": {
                "latitude": "64.4763",
                "longitude": "99.6644"
                },
                "timezone": {
                "offset": "0:00",
                "description": "Western Europe Time, London, Lisbon, Casablanca"
                }
            },
            "email": "esma.daglaroglu@example.com",
            "login": {
                "uuid": "c14374c4-881e-4d17-b2ea-49fbeae26a85",
                "username": "bigpeacock338",
                "password": "toronto",
                "salt": "1pnAvxWS",
                "md5": "f2fabf1ca2b5ca91951e0e75cc22d8ff",
                "sha1": "3194d53d6370a848e0509d06583cf7217b9cbdba",
                "sha256": "2ee0e912ca5fce21291264634f48c37fcc525f7da9bb77cc74b284d49f2116c7"
            },
            "dob": {
                "date": "1952-08-15T14:56:14.367Z",
                "age": 71
            },
            "registered": {
                "date": "2014-06-25T05:23:40.618Z",
                "age": 9
            },
            "phone": "(679)-113-4398",
            "cell": "(698)-016-4436",
            "id": {
                "name": "",
                "value": None
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/women/79.jpg",
                "medium": "https://randomuser.me/api/portraits/med/women/79.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/women/79.jpg"
            },
            "nat": "TR"
            },
            {
            "gender": "male",
            "name": {
                "title": "Mr",
                "first": "Brandon",
                "last": "Newman"
            },
            "location": {
                "street": {
                "number": 2827,
                "name": "Westheimer Rd"
                },
                "city": "Adelaide",
                "state": "Victoria",
                "country": "Australia",
                "postcode": 2830,
                "coordinates": {
                "latitude": "10.6908",
                "longitude": "175.1573"
                },
                "timezone": {
                "offset": "+2:00",
                "description": "Kaliningrad, South Africa"
                }
            },
            "email": "brandon.newman@example.com",
            "login": {
                "uuid": "16ca9e9e-a542-47f9-afed-43656cbe1b42",
                "username": "silverlion127",
                "password": "goofy",
                "salt": "ILAmyGDH",
                "md5": "8500d3522e59737da20d6e76aa3085d4",
                "sha1": "75b48a9036121decacb1f25370939b2f56c4dfba",
                "sha256": "6f8cee7cc7579849424f0a3b079e8667cbc0a51e2e304327375527923e0be572"
            },
            "dob": {
                "date": "1952-08-21T14:48:12.624Z",
                "age": 71
            },
            "registered": {
                "date": "2005-07-03T14:54:04.745Z",
                "age": 18
            },
            "phone": "07-6918-8669",
            "cell": "0429-378-269",
            "id": {
                "name": "TFN",
                "value": "176559092"
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/men/91.jpg",
                "medium": "https://randomuser.me/api/portraits/med/men/91.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/men/91.jpg"
            },
            "nat": "AU"
            }
        ]

@router.get("/randomusers")
def generate_users():
    return {"results": users}

@router.get("/randomusers/{user_id}")
def get_user(user_id: int):
    return users[user_id]

# @router.put("/randomusers/")
# def create_user()
