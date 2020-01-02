# Activation test MEA : Standard Protocol

## Conditions

### MEA STRUCTURE
- Anode: CP (TGP-0120) + Pt/C 20% + 30% Nafion + 1.98 mg DL/cm2 (C29)
- Catalyst loading: 0.377 mg/cm2
- Membrane: Nafion 112
- Cathode: : CP (TGP-0120) + Pt/C 20% + 30% Nafion + 1.98 mg DL/cm2 (C29)
- Catalyst loading: 0.377 mg/cm2

### OPERATION CONDITION
- Ta/ Tc/ Tcell : 60 /50/ 55OC, P= 5 psig, Flow rate H2/O2: 200/200

### ACTIVATION PROCEDURE
1. 10 min OCV
2. 60 min at constant voltage 0.6V
3. cycling potential between 0.7 - 14min and 0.5V - 14 min for 10 times
4. constant current 0.2Acm-2 for 18hr

### OPERATION CONDITION AFTER ACTIVATION
- RH 30%: Ta/ Tc/ Tcell: 80/49/75
- RH 50%: Ta/ Tc/ Tcell: 80/59/75
- RH 100%: Ta/ Tc/ Tcell: 80/75/75
- P= 5psig: flow H2/O2 or air= 200/200
- P= 15psig: flow H2/O2 or air= 300/300
- P= 25psig: flow H2/O2 or air= 500/500


## Files

### 1- Impedance at end of each activation set			

```
Column 1: Zreal

Column 2: Zimaginary

Column 3: Voltage (V)

Column 4: Activation set


```			
	

1. [Data File](1.csv)		

2. [Name File](1.name)


### 2- Impedance at various voltages (1)


```
Column 1: Zreal

Column 2: Zimaginary

Column 3: Voltage (V)

Column 4: Pressure (psi)

Column 5: Relative humidity (RH%)


```

1. [Data File](2.csv)		

2. [Name File](2.name)


### 3- Impedance at various voltages (2)

```
Column 1: Zreal

Column 2: Zimaginary

Column 3: Voltage (V)

Column 4: Pressure (psi)

Column 5: Relative humidity (RH%)


```

1. [Data File](3.csv)		

2. [Name File](3.name)


### 4- Polarization at end of activation procedure (1)

```
Column 1: I (mA/cm²) (Current Density)

Column 2: E_Stack (V) (Voltage)

Column 3: Power (mW/cm²)

Column 4: Pressure (psi)

Column 5: Relative humidity (RH%)

```

1. [Data File](4.csv)		

2. [Name File](4.name)



### 5- Polarization at end of activation procedure (2)

```
Column 1: I (mA/cm²) (Current Density)

Column 2: E_Stack (V) (Voltage)

Column 3: Power (mW/cm²)

Column 4: Pressure (psi)

Column 5: Relative humidity (RH%)

```

1. [Data File](5.csv)		

2. [Name File](5.name)

### 6- Polarization at end of each activation set

```
Column 1: I (mA/cm²) (Current Density)

Column 2: E_Stack (V) (Voltage)

Column 3: Power (mW/cm²)

Column 4: Activation Set

```

1. [Data File](6.csv)		

2. [Name File](6.name)
