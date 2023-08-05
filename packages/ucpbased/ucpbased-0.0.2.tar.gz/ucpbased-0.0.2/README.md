# UCP-Based

This is the first version of UCP-based library.

## Installation

```bazaar
pip install ucpbased
```

## Usage

```python
from ucpbased import UCP

ucp = UCP()
uaw = ucp.input_UAW(0, 0, 5)
uucw = ucp.input_UUCW(0, 29, 0)
uucp = ucp.get_UUCP()

tcf = ucp.input_TFactor(3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 0, 3)
ecf = ucp.input_EFactor(3, 3, 3, 3, 3, 3, 0, 0)

useCasePoints = ucp.get_UCP()
mh = ucp.get_MH(28)

print('UAW     : {:10.2f}'.format(uaw))
print('UUCW    : {:10.2f}'.format(uucw))
print('UUCP    : {:10.2f}'.format(uucp))
print('TFactor : {:10.2f}'.format(tcf))
print('EFactor : {:10.2f}'.format(ecf))
print('UCP     : {:10.2f}'.format(useCasePoints))
print('MH      : {:10.2f}'.format(mh))
```

## Expected output:

```
UAW     :      15.00
UUCW    :     290.00
UUCP    :     305.00
TFactor :       0.93
EFactor :       0.81
UCP     :     231.17
MH      :    6472.89
```