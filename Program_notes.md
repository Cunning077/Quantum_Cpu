A quantum state is the (n)^2, where n represents the amount of qubits the circuit will posess each qubit having its own wire as well.

a basic state is [1,0,0,0] which would return as |00> which would mean both qubits are currently 0, however in practice this is disregarded as the 
 qubits arent in superposition so in theory are treated as a uknown.

since each qubit can either be 1 or 0 the possible states are:
00, 01
10, 11
these are reffered to as computational basis states.

These basis states can then be used to compute the state of the circuit:
    |y> = a_0|00> + a_1|01> + a_2|10> + a_3|11>

during the emulator the actual state of the qubits/ circuit will never be stored simply the amplitudes associated with the qubits as it defeats the purpose of the basis of QM

from there the probability of each state being measured is computed which is the absolute value of each amplitude taken to the exponenent of 2

and in the simulation using these probability i make use of numpy to randomly choose one to essentially decide which state its gonna be in

From there since the circuit has been measured the qubits need to be collapsed to represent that measured state.

from here this is the fundementals of the state itself a measure function a probability function and the actual quantumstate its self

# Fundemental Gates

## Hadamar gate
    H = (1/(2 **(1/2))) [[1,1][1,-1]]

    This means the probability of the amplitudes giving either a 0 or 1 is equal, when thinking of the word equal you would assume that is should be a 50% (
    thats what i originally thought), however the states represent the amplitudes of each chance occuring, not the direct probability for each one. So we 
    have to find what amplitude would give a 50% probability, which was found by taking the absolute value of the amplitude to the exponent of 2:
        (|AMP| ** 2 = p%)  substituted --> |AMP| ** 2 = 0.5 --> AMP = 1 / 2 ** (1/2) --> AMP = 0.707

    Now we know that the amp that would give a equal chance of either case happening is 0.707 know we have to set the state to allow for the change to occur
    To do so we need to eliminate cases where q1 is '1' as it cant be. which leaves us with 2 cases being possible from the original base states:
        00 or 10 , which represent a1 and a2

    Both of these need to be an exact equal chance of happening which was found to be 0.707 so the state is changed to:
        [0.707, 0, 0.707, 0]

    Now in code we make use of identity matrixes, as to properly change the state we need to multiply it by a state equal to its dimensions, and i matrix 
    is essentially just a 1, it wont change the original matrix

    essentially the whole idea is create h and then fill in the remaining columns with i matrixes and simply multiply then (in matrix way lol)

## Not gate
    This gate is dead simple in that it simple just flips the qubit, after a qubit has been superpositioned by the h-gate lets say its assumed to be 1 in
    the first postion, if an x-gate is applied (not-gate) then it becomes 0, and vice versa

    in code this is represented by the matrix:
        [[1,0][0,1]]
    which just flips the values of the original form

    we also make use of the same system as the h-gate 

## Phase flip
    this gate is actually simple in practice but is dead confusing in the way it works as it has no immediate effect, but instead is like placing a passive
    buff on your quantum circuit (weird analogue).

    Basically it switchs the sign of the amps or in theory switches the amplitudes this will not change the general probability straight away but when a 
    double h-gate is applied it can alter the state measured

From here the gates become more complicated as they will start altering multi register amplitudes, or in short it hits two qubits at once

# Two qubit gates

## Cnot gate
    a foundational gate for grovers algorithm, cnot essentially is like a not gate in manner, it has a control and a target.

    if the control is 1 flip the target 
    and if the control is 0 do nothing

    since it is rule based there is no single matrix that can be used however there is still rules that can be followed
        
        - for one lets extract the actual results for each possible amplitude, as we remember a 2 qubit circuit's amplitudes are [00, 01, 10, 11] each of
          these represent something we manipulated with the one qubit bits they all are values or early stage proportions.

        - from this we actually can create a simple rule, if that first bit is a 1 we are gonna do something if its not then we do nothing

        - so when the bit is one we switch its 2nd bit state or in this case '10' becomes '11', so revisting our states if we have [a,b,c,d] it becomes
          [a,b,d,c] so essentially all that would happen is the early stage probabilitys would switch.

        - in addition since its limited to one control and one target realisticly we dont have to look at the full matrix we just need to find n for number
          of qubits.

    so now there is a system how can it be coded:
        define control and target
        so you would think a for loop would be stupid bc surely quantum computing would be diminshed by using a for loop, but luckily no.

        for one an index represented as a bit can hold the state: format(index, f"0{num_q}b") this turns a index like 1 or 3 into the right bit.

        from here use the rules and mark which indexes are considered true and which ones arent and all we do is match the switched ones to its new amp
        
