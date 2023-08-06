# Agent Worker

Framework para implementar agenes con acciones que permitan ejecutarlos bajo un protocolo
basado en json-rpc.

```python

@Agents.Define(options(
    Name = '',
    Kafka = []
))
class Example:

    @Agents.Methods('list')
    def NameMethod(data, Resquest):
        # Response
        return 10
```