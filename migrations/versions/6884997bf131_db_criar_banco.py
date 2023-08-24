"""db_criar_banco

Revision ID: 6884997bf131
Revises: 
Create Date: 2023-08-23 14:17:55.662038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6884997bf131'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cadastro_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.Column('sobrenome', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('cpf', sa.String(length=14), nullable=False),
    sa.Column('telefone', sa.String(length=15), nullable=False),
    sa.Column('endereco_rua', sa.String(length=100), nullable=False),
    sa.Column('endereco_bairro', sa.String(length=50), nullable=False),
    sa.Column('endereco_cidade', sa.String(length=50), nullable=False),
    sa.Column('endereco_uf', sa.String(length=2), nullable=False),
    sa.Column('senha', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('contato_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('telefone', sa.String(length=14), nullable=False),
    sa.Column('mensagem', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contato_model')
    op.drop_table('cadastro_model')
    # ### end Alembic commands ###