import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import *


assistant_JWT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRLWDlsd3JmYnJlMlE0SlhOQmNaciJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlZDQwNTcwZWU5MjAwMDEzNGY5ZDdjIiwiYXVkIjoiZGV2IiwiaWF0IjoxNTkzNjY1ODQ3LCJleHAiOjE1OTM3NTIyNDcsImF6cCI6IjREd1cwc00zQ3prOHVyNktZMVZRdmJXeDZsMlhjSTREIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0cm9zIiwiZ2V0Om1vdmllIl19.kz228WnVImtUT3fjUe2Uky9MISbRpul6LbSIvLzvDl6NaV0Gtqyym56uqqFQvfMjuCnfuV-E-1rZgL-UrP7cp11n5eS8nw1KJxpKk8Bv-miNQNRowucmFfH7vHYi028AHaCCP9Xlr8KHV0q3kpmReu16zT5WN32Ky3UE89q_Cs-AZfiy7CWVqxAzhVxx98HnOkPSKTCRiQX7nx2yZNLK3Tvw_3wMQtCPR9i_PuEXruql98KKUdlGKEf79kSujhp1zi_ZS0jf7C4eJ8VYxATuTQqs9PdrELpCeOy5lyBmOfzl56rx4EjQrMFC2N01Ha02dLVlaRRCXG9brPvTtrtK9w'
director_JWT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRLWDlsd3JmYnJlMlE0SlhOQmNaciJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlZDRlYThiNzcyNWIwMDEzNDA4ZDY0IiwiYXVkIjoiZGV2IiwiaWF0IjoxNTkzNjY1MDU4LCJleHAiOjE1OTM3NTE0NTgsImF6cCI6IjREd1cwc00zQ3prOHVyNktZMVZRdmJXeDZsMlhjSTREIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0cm9zIiwiZ2V0OmFjdHJvcyIsImdldDptb3ZpZSIsInBhdGNoOmFjdHJvcyIsInBhdGNoOm1vdmllIiwicG9zdDphY3Ryb3MiXX0.CvDgsVktJchWhOTpGa4WuMNyEjfdPLB9N6g3sX5Gahk-VniDVAFSZNvaMLs9yWzaVDo-B-ia8SFKIgdGOINIDYfg-_b5ELvymu89pvQNHSEd1IKdbtFEkbbbC5f8UohIBZ8V7WIOjD8vAfKo6-INoWOF_mHY-YTglPguR0z7fHQ85poh1XVn8QJ0N2T_cVU4qI8PcqSrezSE-RFBziEiVsKii6IWegpd5R--Ao8qjpF3k3jz_xmHjzW3mhml1sr7Vt3f5QaWe2euVUjTYIESmka_eMcH3X8HGgGlPdvnzz-zxlwZp134wdyEMbpn6geILBtK8dBapfjdsf80es2QsA'
producer_JWT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRLWDlsd3JmYnJlMlE0SlhOQmNaciJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmYzk1N2ZiMzI3YjMwMDEzZTkzNTgzIiwiYXVkIjoiZGV2IiwiaWF0IjoxNTkzNjY1MjY2LCJleHAiOjE1OTM3NTE2NjYsImF6cCI6IjREd1cwc00zQ3prOHVyNktZMVZRdmJXeDZsMlhjSTREIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0cm9zIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdHJvcyIsImdldDptb3ZpZSIsInBhdGNoOmFjdHJvcyIsInBhdGNoOm1vdmllIiwicG9zdDphY3Ryb3MiLCJwb3N0Om1vdmllIl19.tj1MGpe8Ku5B4OrOtkXuHVFFE_tYVc9GTYs7PwjyguPfjL8_eqsdIglk_C2yXid90DAGvKIeIrYuUg--wGZMqqTkgVzBOAkXnq77som4PNkWEn-PVtyBmp82jVa7qhkN0GKbnzI7H48rPM7ye_uKRzKCyDMbJYucUG_piyS5TTW9qk2bkslacuveeXv51EToEy_wxWmEobPErMFXpz2WLMyBZ76VWUFTGAqzC354GVjYRaIaQ7G-XgGLdzx1z_APl28-kgFzOq9KTG3IlrkTRHC3FAbvC8Sn_7U4VlDMuffEtnNp1NBgDrt68qx5WajAMGbHm9vXtcgVS82yqBZbzw'


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'udacity', 'localhost:5432', database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
          'name': 'Abdullah',
          'age': 15,
          'gender': 'Male'
        }


        self.edit_actor = {
          'name': 'Alessa',
          'age': 51,
          'gender': 'Male'
        }

        self.new_movie = {
          'title': "covid19",
          'release_date': "2019-11-11 11:00"
        }

        self.edit_movie = {
          'title': "old movie",
          'release_date': "2020-1-1 01:00"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_all_actors(self):
        res = self.client().get('/actros',headers={"Authorization": assistant_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(type(data['actros_info']) is list)

    def test_get_all_actors_error_401(self):
        res = self.client().get('/actros')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_all_movies(self):
        res = self.client().get('/movie',headers={"Authorization": assistant_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies_info'])

    def test_get_all_movies_error_401(self):
        res = self.client().get('/movie')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_actor(self):
        res = self.client().post('/actros', json=self.new_actor, headers={"Authorization": director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actros_info'])

    def test_create_movie(self):
        res = self.client().post('/movie', json=self.new_movie, headers={"Authorization": producer_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['movies_info'])

    def test_create_actor_error_401(self):
        res = self.client().post('/actros', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_movie_error_401(self):
        res = self.client().post('/movie', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_actor_error_403(self):
        res = self.client().post('/actros', json=self.new_actor, headers={"Authorization": assistant_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_create_movie_error_403(self):
        res = self.client().post('/movie', json=self.new_movie, headers={"Authorization": director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


    def test_edit_actors(self):
        new_actros = Actor(name = "AbdullahAlessa" , age = 25 , gender = "Male")
        new_actros.insert()
        res = self.client().patch(f'/actros/{new_actros.id}', json=self.edit_actor, headers={"Authorization":  director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['Actor_info'])

    def test_edit_movies(self):
        new_movie = Movie(title = "Covid" , release_date="2019-11-12 11:00")
        new_movie.insert()
        res = self.client().patch(f'/movie/{new_movie.id}', json=self.edit_movie,headers={"Authorization": producer_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)


    def test_edit_actors_error_404(self):
        res = self.client().patch('/actros/500', json=self.edit_actor, headers={"Authorization":  director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_edit_movies_error_404(self):
        res = self.client().patch('/movie/500', json=self.edit_movie, headers={"Authorization": director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actors(self):
        new_actros = Actor(name = "AbdullahAlessa" , age = 25 , gender = "Male")
        new_actros.insert()
        res = self.client().delete(f'/actros/{new_actros.id}', headers={"Authorization": director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['delete'], str(new_actros.id))

    def test_delete_movies(self):
        new_movie = Movie(title = "Covid" , release_date="2019-11-12 11:00")
        new_movie.insert()
        res = self.client().delete(f'/movie/{new_movie.id}', headers={"Authorization": producer_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)

    def test_delete_actors_error_404(self):
        res = self.client().delete('/actros/2020', headers={"Authorization": director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)

    def test_delete_movies_error_404(self):
        res = self.client().delete('/movie/2020', headers={"Authorization": producer_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)

    def test_delete_actors_error_403(self):
        res = self.client().delete('/actros/1', headers={"Authorization": assistant_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'],False)

    def test_delete_movies_error_403(self):
        res = self.client().delete('/movie/1', headers={"Authorization": director_JWT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'],False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()