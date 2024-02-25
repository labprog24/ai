class State:
    def __init__(self,monkey_loc , monkey_on_box , box_loc , monkey_has_banana):
        self.monkey_loc = monkey_loc
        self.monkey_on_box = monkey_on_box
        self.box_loc=box_loc
        self.monkey_has_banana = monkey_has_banana

    def __str__(self):
        return f"Monkey:{self.monkey_loc},on box:{self.monkey_on_box},Box:{self.box_loc},Has Banana:{self.monkey_has_banana}"


def grasp(state):
    state.monkey_has_banana=True
    return state

def climb(state):
    state.monkey_on_box=True
    return state

def drag(state,P1,P2):
    state.box_loc=P2
    return state

def walk(state, P1, P2):
    state.monkey_loc=P2
    return state

def can_get(state):
    return state.monkey_has_banana

def solve():
    ins= State("middle",False,"middle",False)
    state1=walk(ins,"left","right")
    print(f"Step 1:{state1}")
    state2=drag(state1, "middle", "right")
    print(f"Step 2:{state2}")
    state3=climb(state2)
    print(f"Step 3:{state3}")
    state4=grasp(state3)
    print(f"Step 4:{state4}")

    if can_get(state4):
        print("GOal reached: Moneky has  the banana!")
    else:
        print("goal not reached")

solve()
    
        
        
