from database import get_database
# from dotenv import load_dotenv 
#load_dotenv('.env')

db = get_database()

restaurants = db['restaurants']
openings = db['restaurantsOpenings']

# #Cargando los JSON para insertar
# with open('data/restaurants.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# #Insertar los JSON, da problemas
# restaurants.insert_many(data)

def consulta1():
    result = restaurants.aggregate([
    {
        '$group': {
            '_id': {
                'sector': '$borough', 
                'tipo_cocina': '$cuisine'
            }, 
            'count': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'count': -1
        }
    }
])
    return list(result)

def consulta2():
  result = restaurants.aggregate([
  {'$project': {
    '_id':0,
    'name': 1,
    'rating': {'$avg': "$grades.score"}
  }},
  {'$sort': {'rating': -1}},
  {'$limit': 5}
])
  return list(result)

def consulta3():
  result = restaurants.aggregate([
  {'$project': {
    'name': 1,
    'rating': {'$avg': "$grades.score"}
  }},
  {'$sort': {'rating': -1}},
  {'$limit': 50},
  {'$project': {
    'name': 1,
    'rating': 1,
    'calificacion': {
      '$cond': {
        'if': {'$gt': ["$rating", 20]},
        'then': "A",
        'else': {'$cond': {
          'if': {'$gt': ["$rating", 13]},
          'then': "B",
          'else': "C"
        }}
      }
    }
  }}
])
  return list(result)

def consulta4(): 
  result = restaurants.aggregate([
  {'$unwind': "$grades"},
  {'$sort': {"grades.date": 1}},
  {'$limit': 1},
  {'$project': {"_id": 0, "oldest_review": "$grades"}}
])
  return list(result)

def consulta5(): 
  result = openings.aggregate([
  { '$unwind': { 'path': "$operating_hours" } },
  {
    '$project': {
      '_id': 0,
      'name': 1,
      'closed': {
        '$switch': {
          'branches': [
            {
              'case': {
                '$eq': [
                  "$operating_hours.Monday",
                  "Closed",
                ],
              },
              'then': "Monday",
            },
            {
              'case': {
                '$eq': [
                  "$operating_hours.Tuesday",
                  "Closed",
                ],
              },
              'then': "Tuesday",
            },
            {
              'case': {
                '$eq': [
                  "$operating_hours.Wednesday",
                  "Closed",
                ],
              },
              'then': "Wednesday",
            },
            {
              'case': {
                '$eq': [
                  "$operating_hours.Thursday",
                  "Closed",
                ],
              },
              'then': "Thursday",
            },
            {
              'case': {
                '$eq': [
                  "$operating_hours.Friday",
                  "Closed",
                ],
              },
              'then': "Friday",
            },
            {
              'case': {
                '$eq': [
                  "$operating_hours.Saturday",
                  "Closed",
                ],
              },
              'then': "Saturday",
            },
            {
              'case': {
                '$eq': [
                  "$operating_hours.Sunday",
                  "Closed",
                ],
              },
              'then': "Sunday",
            },
          ],
          'default': "Open Everyday",
        },
      },
    },
  },
])
  return list(result)


# print(list(consulta1))
# print()
# print(list(consulta2))
# print
# print(list(consulta3))
# print
# print(list(consulta4))
# print
# print(list(consulta5))
