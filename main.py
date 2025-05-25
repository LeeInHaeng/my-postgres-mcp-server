# mcp server tutorial youtube ref : https://www.youtube.com/watch?v=9ucmgQRVkwo

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import psycopg2
import json
import os

mcp = FastMCP("pgsql-executor")

load_dotenv()
pgsql_user = os.getenv("PGSQL_USER")
if not pgsql_user:
    raise ValueError("pgsql_user is not set in environment")
pgsql_password = os.getenv("PGSQL_PASSWORD")
if not pgsql_password:
    raise ValueError("pgsql_password is not set in environment")
default_executor_file_dir = os.getenv("DEFAULT_EXECUTOR_FILE_DIR")
if not default_executor_file_dir:
    raise ValueError("default_executor_file_dir is not set in environment")

def execute_sql_file(filename: str) -> str:
    # PostgreSQL 연결 정보
    conn = psycopg2.connect(
        dbname="Review",
        user=pgsql_user,
        password=pgsql_password,
        host="localhost",
        port="5432"
    )

    try:
        with conn:
            with conn.cursor() as cur:
                with open(f"{default_executor_file_dir}\\{filename}", 'r', encoding='utf-8') as file:
                    sql = file.read()
                    cur.execute(sql)

                    # select
                    if cur.description:
                        rows = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        result = [dict(zip(columns, row)) for row in rows]
                        json_string = json.dumps(result, ensure_ascii=False)
                        return json_string
                    # insert , update , delete
                    else:
                        return f"{cur.rowcount} rows affected."
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        conn.close()

# mcp 에 제공할 툴
@mcp.tool()
def pgsql_query_execute(filename: str) -> str:
    # 해당부분의 주석 중요 : AI 에서 주석을 읽고 이게 어떤 기능인지 확인한다.
    """
    Returns .sql 확장자의 파일 이름을 제공하면, 그 파일의 내용을 읽어 postgresql 에서 해당 쿼리를 실행 후 결과를 반환한다.
    select 일 경우 json 을 string으로 변경한 형식으로 반환된다.
    select 의 예시 : [{"id": 1, "name": "테스트1"}, {"id": 2, "name": "테스트2"}]
    insert , update , delete 는 몇개의 row 가 영향을 받았는지 반환된다.
    에러일 경우 Error: 에러 메세지로 반환 된다.

    :param filename: .sql 확장자로된 파일명
    """
    return execute_sql_file(filename)

if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run(transport="stdio")