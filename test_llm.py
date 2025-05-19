from omniagent.llm.llm_provider import LLMProvider

def test_llm():
    try:
        llm = LLMProvider.get_llm()
        print("✅ Successfully got LLM instance:", llm)

        prompt = "Write a short poem about AI."
        output = llm.run(prompt)
        print("✅ LLM output:\n", output)

    except Exception as e:
        print("❌ Error testing LLM:", e)

if __name__ == "__main__":
    test_llm()
