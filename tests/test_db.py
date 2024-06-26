from sqlalchemy import select

from fast_api_zero.models import User


def test_create_user(session):
    user = User(
        username='Henrique',
        email='test@test.com',
        password='minha_senha',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'test@test.com')
    )

    assert result.id == 1
    assert result.username == 'Henrique'
    assert result.password == 'minha_senha'
