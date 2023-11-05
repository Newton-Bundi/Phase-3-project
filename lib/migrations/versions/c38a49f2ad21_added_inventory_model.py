"""Added Inventory model

Revision ID: c38a49f2ad21
Revises: 0a19ba1840f0
Create Date: 2023-11-05 15:05:28.249567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c38a49f2ad21'
down_revision = '0a19ba1840f0'
branch_labels = None
depends_on = None


def upgrade():
# Create the products table
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('price', sa.Integer),
        sa.Column('quantity', sa.Integer, server_default='0'),
        sa.Column('supplier_id', sa.Integer, sa.ForeignKey('suppliers.id'))
    )

    # Create the suppliers table
    op.create_table(
        'suppliers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('contact_info', sa.String)
    )

    # Create the orders table
    op.create_table(
        'orders',
        sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id'), primary_key=True),
        sa.Column('order_date', sa.Date, primary_key=True),
        sa.Column('quantity', sa.Integer)
    )


def downgrade():
    # Define the table drop statements for downgrading the migration
    op.drop_table('orders')
    op.drop_table('products')
    op.drop_table('suppliers')
