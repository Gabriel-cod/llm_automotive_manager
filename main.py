from models.automotive_model import Base, engine, populate_db_with_fictitious_data
from client.client_setup import agent
from prompt_toolkit import PromptSession

def run_chat():
    session = PromptSession()
    print("""\n\nBem vindo(a) à locadora de veículos! \nEu sou sua agente virtual e estou aqui para ajudá-lo a
encontrar o veículo ideal para você. (digite 'sair' para encerrar):\n""")
    while True:
        try:
            user_input = session.prompt("> ")
            if str(user_input).lower().strip() in ["sair", "exit", "quit"]:
                break
            response = agent.run(user_input)
            print(response)
        except Exception as e:
            print(f"[ERRO] {e}")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    populate_db_with_fictitious_data()
    run_chat()
