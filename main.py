from mcp.server.fastmcp import Context, FastMCP

# 初始化 FastMCP 服务器
mcp = FastMCP("mcp", host="0.0.0.0", port=8024)


@mcp.tool()
async def test_info(
    query: str,
    ctx: Context = None,
) -> dict:

    print(f"mcp-测试开始, request_id: {ctx.request_id}")
    res = {"query": query, "id_echo": ctx.request_id}

    return res


if __name__ == "__main__":

    mcp.run(transport="sse")
