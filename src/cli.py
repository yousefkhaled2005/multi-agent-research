import argparse
from src.graph import ResearchOrchestrator


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Research Engine CLI")
    parser.add_argument("--topic", type=str, required=True, help="Research topic or question")
    parser.add_argument("--lang", type=str, default="ar", choices=["ar", "en"], help="Target language")
    args = parser.parse_args()

    orchestrator = ResearchOrchestrator()
    print(f"[*] Initiating multi-agent research workflow on: {args.topic}...")
    result = orchestrator.run(topic=args.topic, language=args.lang)

    print("\n================ FINAL REPORT ================\n")
    print(result.get("final_report"))
    print("\n==============================================\n")


if __name__ == "__main__":
    main()
