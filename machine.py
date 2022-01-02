from fsm import TocMachine

def new_machine():
    machine = TocMachine(
        states=["main_menu", "breakfast", "hamberger", "b_info", "b_price", "b_health", "h_info", "h_price", "h_health"],
        transitions=[
            {
                "trigger": "advance",
                "source": ["main_menu", "breakfast", "hamberger","b_info", "b_price", "b_health", "h_info", "h_price", "h_health"],
                "dest": "main_menu",
                "conditions": "is_going_to_main_menu",
            },
            {
                "trigger": "advance",
                "source": ["main_menu", "b_info", "b_price", "b_health"],
                "dest": "breakfast",
                "conditions": "is_going_to_breakfast",
            },
            {
                "trigger": "advance",
                "source": ["main_menu", "h_info", "h_price", "h_health"],
                "dest": "hamberger",
                "conditions": "is_going_to_hamberger",
            },
            {
                "trigger": "advance",
                "source": "breakfast",
                "dest": "b_info",
                "conditions": "is_going_to_b_info",
            },
            {
                "trigger": "advance",
                "source": "hamberger",
                "dest": "h_info",
                "conditions": "is_going_to_h_info",
            },
            {
                "trigger": "advance",
                "source": ["b_info", "b_health"],
                "dest": "b_price",
                "conditions": "is_going_to_b_price",
            },
            {
                "trigger": "advance",
                "source": ["h_info", "h_health"],
                "dest": "h_price",
                "conditions": "is_going_to_h_price",
            },
            {
                "trigger": "advance",
                "source": ["b_info", "b_price"],
                "dest": "b_health",
                "conditions": "is_going_to_b_health",
            },
            {
                "trigger": "advance",
                "source": ["h_info", "h_price"],
                "dest": "h_health",
                "conditions": "is_going_to_h_health",
            },
        ],
        initial="main_menu",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine