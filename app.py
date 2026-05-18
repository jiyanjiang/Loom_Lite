import gradio as gr

def hello(x):
    return "Loom_Lite ready: " + x

demo = gr.Interface(fn=hello, inputs="text", outputs="text")
demo.launch()