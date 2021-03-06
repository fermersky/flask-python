"""empty message

Revision ID: 64835a3364b9
Revises: 97b39f8dcd0a
Create Date: 2022-02-06 18:47:17.292816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "64835a3364b9"
down_revision = "97b39f8dcd0a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("fullname", sa.Text(), nullable=True),
        sa.Column("email", sa.Text(), nullable=True),
        sa.Column("password", sa.Text(), nullable=True),
        sa.Column("salt", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("user")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("fullname", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("email", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("password", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("salt", sa.TEXT(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
    )
    op.drop_table("users")
    # ### end Alembic commands ###
