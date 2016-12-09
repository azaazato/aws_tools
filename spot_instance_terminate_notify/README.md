# notify spot instance terminate

## Setup

```
sudo cp spot-notify /usr/bin
sudo cp check-terminate /etc/init.d/
sudo chkconfig --add check-terminate
sudo chkconfig check-terminate on
```
