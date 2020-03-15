# Activation Test MEA : Standard Protocol

## Conditions

### MEA STRUCTURE
- Anode: CP (TGP-0120) + Pt/C 20% + 30% Nafion + 1.98 mg DL/cm2 (C29)
- Catalyst loading: 0.377 mg/cm2
- Membrane: Nafion 112
- Cathode: : CP (TGP-0120) + Pt/C 20% + 30% Nafion + 1.98 mg DL/cm2 (C29)
- Catalyst loading: 0.377 mg/cm2

### OPERATION CONDITION
- Ta/ Tc/ Tcell : 60 /50/ 55 C, P= 5 psig, Flow rate H2/O2: 200/200 ml/min

### ACTIVATION PROCEDURE
1. 10 min OCV
2. 60 min at constant voltage 0.6V
3. Cycling potential between 0.7 - 14min and 0.5V - 14 min for 10 times
4. Constant current 0.2Acm-2 for 18hr

Each activation set contains a repetition of the items of activation procedure. 24 sets, 24 repetition. 

### OPERATION CONDITION AFTER ACTIVATION
- RH 30%: Ta/ Tc/ Tcell: 80/49/75 C
- RH 50%: Ta/ Tc/ Tcell: 80/59/75 C
- RH 100%: Ta/ Tc/ Tcell: 80/75/75 C 
- P= 5psig: flow H2/O2 or air= 200/200 ml/min
- P= 15psig: flow H2/O2 or air= 300/300 ml/min
- P= 25psig: flow H2/O2 or air= 500/500 ml/min


## Files

### 1- Impedance : End of Each Activation Set			

```
Column 1: Zreal (ohm)

Column 2: Zimaginary (ohm)

Column 3: Applied voltage (V)

Column 4: Activation set
```			
	

1. [Data File](1.csv)		

2. [Names File](1.names)


### 2- Impedance : Various Voltages (1)


```
Column 1: Zreal (ohm)

Column 2: Zimaginary (ohm)

Column 3: Applied voltage (V)

Column 4: Pressure (psig)

Column 5: Relative humidity (RH%)
```

1. [Data File](2.csv)		

2. [Names File](2.names)


### 3- Impedance : Various Voltages (2)

```
Column 1: Zreal (ohm)

Column 2: Zimaginary (ohm)

Column 3: Applied voltage (V)

Column 4: Pressure (psig)

Column 5: Relative humidity (RH%)
```

1. [Data File](3.csv)		

2. [Names File](3.names)


### 4- Polarization : End of Activation Procedure (1)

```
Column 1: Current density (mA/cm²)

Column 2: Cell voltage (V)

Column 3: Power density (mW/cm²)

Column 4: Pressure (psig)

Column 5: Relative humidity (RH%)
```

1. [Data File](4.csv)		

2. [Names File](4.names)



### 5- Polarization : End of Activation Procedure (2)

```
Column 1: Current density (mA/cm²)

Column 2: Cell voltage (V)

Column 3: Power density (mW/cm²)

Column 4: Pressure (psig)

Column 5: Relative humidity (RH%)
```

1. [Data File](5.csv)		

2. [Names File](5.names)

### 6- Polarization : End of Each Activation Set

```
Column 1: Current density (mA/cm²)

Column 2: Cell voltage (V)

Column 3: Power density (mW/cm²)

Column 4: Activation set
```

1. [Data File](6.csv)		

2. [Names File](6.names)
