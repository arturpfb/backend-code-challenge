"""creates test db

Revision ID: 474ec52a86b7
Revises: 
Create Date: 2023-02-02 00:44:30.512695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "474ec52a86b7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
            CREATE TABLE IF NOT EXISTS public.codechallenge
            (
                id                      SERIAL NOT NULL
                                        CONSTRAINT codechallenge_pkey
                                        PRIMARY KEY,
                name                    VARCHAR(20),
                last_modified_db        TIMESTAMPTZ DEFAULT NOW(),
                created_date_db         TIMESTAMPTZ DEFAULT NOW()
            );
        """
    )


def downgrade():
    op.execute("DROP TABLE IF EXISTS public.codechallenge")
