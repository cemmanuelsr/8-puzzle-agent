from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_docs():
    response = client.get('/docs')
    assert response.status_code == 200

def test_solver():
    response = client.get('/solve/BuscaGananciosa/EuclidianBetter',
                          params = {
                              'table': '8, 3, 6, 7, 5, 4, 2, 1, 0'
                          })
    assert response.status_code == 200
    assert response.json()['path'] == ' ; 0 <--> 1 ; 0 <--> 2 ; 0 <--> 7 ; 0 <--> 8 ; 0 <--> 3 ; 0 <--> 6 ; 0 <--> 4 ; 0 <--> 5 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 5 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 5 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 6 ; 0 <--> 4 ; 0 <--> 5 ; 0 <--> 6 ; 0 <--> 8 ; 0 <--> 3 ; 0 <--> 1 ; 0 <--> 2 ; 0 <--> 4 ; 0 <--> 8 ; 0 <--> 3 ; 0 <--> 1 ; 0 <--> 2 ; 0 <--> 3 ; 0 <--> 8 ; 0 <--> 4 ; 0 <--> 3 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 8'
    assert response.json()['time'] < 0.1

def test_scrambler():
    response = client.get('/shuffle',
                          params = {
                              'table': '1, 2, 3, 8, 0, 4, 7, 6, 5'
                          })
    assert response.status_code == 200
