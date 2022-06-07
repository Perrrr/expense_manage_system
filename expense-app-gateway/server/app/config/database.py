
import asyncpg


pg_connection_db = f"postgresql://n0ksoftDev:noksoftPassw0rd13@expense-app-db/expense-app-db"


async def create_connection() -> asyncpg.Connection:
     con = await asyncpg.connect(dsn=pg_connection_db)
     return con

async def close_connection(con) -> None:
    await con.close()

