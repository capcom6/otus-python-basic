"""Added created_at column

Revision ID: a08437d40f20
Revises: 39764044b702
Create Date: 2022-06-12 14:45:53.334039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a08437d40f20"
down_revision = "39764044b702"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "posts",
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("posts", "created_at")
    # ### end Alembic commands ###
