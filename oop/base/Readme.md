## Protocol vs ABC (abstract base class) vs Interface

If you want to define structures without actually implementation you can choose any of these


| Feature        | Protocol | ABC     | interface |
| -------------- | -------- | ------- | -- ------ |
| Structural     | Yes      | No      | No        |
| Need inherit   | No       | Yes     | Yes       |
| Runtime check  | Partial  | Yes     | Yes       |
| Can be Generic | Yes      | Partial | Yes       |

