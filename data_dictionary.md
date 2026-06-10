# Data Dictionary

## AI4I 2020 Predictive Maintenance Dataset

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| UDI | Integer | Unique identifier for each record | 1 |
| Product ID | String | Unique product identification code | M14860 |
| Type | Categorical | Product quality type (L = Low, M = Medium, H = High) | M |
| Air temperature [K] | Float | Ambient air temperature measured in Kelvin | 298.1 |
| Process temperature [K] | Float | Process temperature measured in Kelvin | 308.6 |
| Rotational speed [rpm] | Integer | Rotational speed of the machine in revolutions per minute | 1551 |
| Torque [Nm] | Float | Torque applied by the machine in Newton-meters | 42.8 |
| Tool wear [min] | Integer | Tool wear duration in minutes | 0 |
| Machine failure | Binary (0/1) | Indicates whether machine failure occurred (1 = Failure, 0 = No Failure) | 0 |
| TWF | Binary (0/1) | Tool Wear Failure indicator | 0 |
| HDF | Binary (0/1) | Heat Dissipation Failure indicator | 0 |
| PWF | Binary (0/1) | Power Failure indicator | 0 |
| OSF | Binary (0/1) | Overstrain Failure indicator | 0 |
| RNF | Binary (0/1) | Random Failure indicator | 0 |

---

## Feature Categories

### Identification Features
- UDI
- Product ID
- Type

### Sensor Features
- Air temperature [K]
- Process temperature [K]
- Rotational speed [rpm]
- Torque [Nm]
- Tool wear [min]

### Target Variable
- Machine failure

### Failure Type Indicators
- TWF (Tool Wear Failure)
- HDF (Heat Dissipation Failure)
- PWF (Power Failure)
- OSF (Overstrain Failure)
- RNF (Random Failure)

---

## Target Variable Description

| Value | Meaning |
|---------|---------|
| 0 | No Machine Failure |
| 1 | Machine Failure |

## Product Type Description

| Type | Meaning |
|------|---------|
| L | Low Quality Product |
| M | Medium Quality Product |
| H | High Quality Product |
