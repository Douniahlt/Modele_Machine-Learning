import math
from pomegranate import *



rain = DiscreteDistribution({"None": 0.4, "light": 0.5, "heavy": 0.1})

maintenance = ConditionalProbabilityTable(
    [["None", "yes", 0.2], ["None", "no", 0.8],
     ["light", "yes", 0.4], ["light", "no", 0.6],
     ["heavy", "yes", 0.2], ["heavy", "no", 0.8]], [rain])

train = ConditionalProbabilityTable(
    [["None", "yes", "Ontime", 0.5], ["None", "yes", "Delayed", 0.5],
     ["None", "no", "Ontime", 0.8], ["None", "no", "Delayed", 0.2],
     ["light", "yes", "Ontime", 0.5], ["light", "yes", "Delayed", 0.5],
     ["light", "no", "Ontime", 0.4], ["light", "no", "Delayed", 0.6],
     ["heavy", "yes", "Ontime", 0.3], ["heavy", "yes", "Delayed", 0.7],
     ["heavy", "no", "Ontime", 0.5], ["heavy", "no", "Delayed", 0.5]], [rain, maintenance])

appointment = ConditionalProbabilityTable(
    [["Ontime", "Attend", 0.8], ["Ontime", "Miss", 0.2],
     ["Delayed", "Attend", 0.7], ["Delayed", "Miss", 0.3]], [train])


s1 = State(rain, name="rain")
s2 = State(maintenance, name="maintenance")
s3 = State(train, name="train")
s4 = State(appointment, name="appointment")


attendance_network = BayesianNetwork("attendance network")
attendance_network.add_states(s1, s2, s3, s4)
attendance_network.add_edge(s1, s2)
attendance_network.add_edge(s1, s3)
attendance_network.add_edge(s2, s3)
attendance_network.add_edge(s3, s4)
attendance_network.bake()


probability_miss = attendance_network.predict_proba({"rain": "light", "maintenance": "no", "train": "Delayed"})[3].parameters[0]["Miss"]
probability_attend = attendance_network.predict_proba({"rain": "light", "maintenance": "no", "train": "Delayed"})[3].parameters[0]["Attend"]

print("P(light, no, Delayed, Miss):", probability_miss)
print("P(light, no, Delayed, Attend):", probability_attend)


print("\nInference for 'train: Delayed':")
print(attendance_network.predict_proba({"train": "Delayed"}))

print("\nInference for 'rain: heavy, train: Delayed':")
print(attendance_network.predict_proba({"rain": "heavy", "train": "Delayed"}))


    



