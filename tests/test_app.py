from fast_zero.schemas import UserPublic


def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


# def test_create_user(client):
#     response = client.post(
#         '/users',
#         json={
#             'username': 'alice',
#             'email': 'alice@example.com',
#             'password': 'secret',
#         },
#     )
#     assert response.status_code == 201
#     assert response.json() == {
#         'username': 'alice',
#         'email': 'alice@example.com',
#         'id': 1,
#     }

#     # Tentativa de criar o mesmo usuário deve falhar
#     response = client.post(
#         '/users/',
#         json={
#             'username': 'alice',
#             'email': 'alice@example.com',
#             'password': 'secret',
#         },
#     )
#     assert response.status_code == 400
#     assert response.json() == {'detail': 'Email already registered'}


# def test_read_users(client):
#     response = client.get('/users')
#     assert response.status_code == 200
#     assert response.json() == {'users': []}


# def test_update_user(client, user, token):
#     response = client.put(
#         f'/users/{user.id}',
#         headers={'Authorization': f'Bearer {token}'},
#         json={
#             'username': 'bob',
#             'email': 'bob@example.com',
#             'password': 'mynewpassword',
#         },
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         'username': 'bob',
#         'email': 'bob@example.com',
#         'id': 1,
#     }


# # def test_update_nonexistent_user(client):
# #     response = client.put(
# #         '/users/999',
# #         json={
# #             'username': 'nonexistent',
# #             'email': 'nonexistent@example.com',
# #             'password': 'password',
# #         },
# #     )
# #     assert response.status_code == 401
# #     assert response.json() == {'detail': 'Not enough permissions'}


# def test_delete_user(client, user, token):
#     response = client.delete(
#         f'/users/{user.id}',
#         headers={'Authorization': f'Bearer {token}'},
#     )

#     assert response.status_code == 200
#     assert response.json() == {'detail': 'User deleted'}

#     # response = client.delete('/users/999')
#     # assert response.status_code == 404
#     # assert response.json() == {'detail': 'User not found'}


# def test_read_users_with_users(client, user):
#     user_schema = UserPublic.model_validate(user).model_dump()
#     response = client.get('/users/')
#     assert response.json() == {'users': [user_schema]}


# def test_get_token(client, user):
#     response = client.post(
#         '/auth/token',
#         data={'username': user.email, 'password': user.clean_password},
#     )
#     token = response.json()

#     assert response.status_code == 200
#     assert 'access_token' in token
#     assert 'token_type' in token
