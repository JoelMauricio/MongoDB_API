from database import get_database

db = get_database()

restaurants = db['restaurants']
openings = db['restaurantsOpenings']

tipos_cocina_sector = restaurants.aggregate([
   {'$group':
     {'_id': {'sector': "$borough", 'tipo_cocina': "$cuisine"},
      'count': {'$sum': 1}
     }
   },
   {'$sort': {'count': -1}}
])

Top_5_puntaje = restaurants.aggregate([
  {'$project': {
    '_id':0,
    'name': 1,
    'rating': {'$avg': "$grades.score"}
  }},
  {'$sort': {'rating': -1}},
  {'$limit': 5}
])

restaurantes_por_puntaje = restaurants.aggregate([
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

review_antiguo = restaurants.aggregate([
  {'$unwind': "$grades"},
  {'$sort': {"grades.date": 1}},
  {'$limit': 1},
  {'$project': {"_id": 0, "oldest_review": "$grades"}}
])

dias_cierran = openings.aggregate([
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


# print(list(tipos_cocina_sector))
# print()
# print(list(Top_5_puntaje))
# print
# print(list(restaurantes_por_puntaje))
# print
# print(list(review_antiguo))
# print
print(list(dias_cierran))
