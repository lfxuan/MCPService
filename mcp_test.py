import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def run_test():
    async with sse_client("http://localhost:8024/sse") as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化
            await session.initialize()
            
            # 列出工具确认是否存在
            tools = await session.list_tools()
            print(f"可用工具: {tools}")

            # 调用你的工具
            # 参数：工具名称test_info、参数值arguments
            result = await session.call_tool("test_info", arguments={"query": "test from client"})
            print(f"调用结果: {result}")

if __name__ == "__main__":
    asyncio.run(run_test())