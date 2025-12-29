from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from compilegraph import app
from typing import Any, Dict
from fastapi.responses import JSONResponse

# 实例化 FastAPI 应用
fastapi_app = FastAPI()

# 允许前端跨域请求（可根据实际情况调整 origins）
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_app.post("/api/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")
    if not question.strip():
        return {"answer": "问题不能为空"}
    
   
    inputs = {"question": question}
    results = []
    final_generation = None

    for output in app.stream(inputs):
        step_result = {}
        for key, value in output.items():
            step_result[key] = {
                "generation": value.get("generation"),
                # 可添加更多内容
            }
            # 最后一次的generation作为最终输出
            final_generation = value.get("generation")
            '''
        results.append(step_result)
    answer = getattr(results, "content", "未找到答案")
    print(answer)
    return {"answer": answer}
    
    return JSONResponse({
        "steps": results,
        "final_generation": final_generation
    })
'''
    app.get_graph().draw_mermaid_png(output_file_path="./images/my_flow.png")
    return JSONResponse({
        "answer": final_generation
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=3001)