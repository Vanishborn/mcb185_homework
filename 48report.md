# Dungeons and Dragons Statistics Report
### by Henry Li

## 1. DND Stats

Explored different ways of rolling stats:
- 3D6: roll 3 six-sided dice
- 3D6r1: roll 3 six-sided dice, but re-roll any 1s
- 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
- 4D6d1: roll 4 six-sided dice, dropping the lowest die roll

Average stats obtained using these rules:
- 3D6: 10.495374
- 3D6r1: 11.749674
- 3D6x2: 13.416952
- 4D6d1: 12.246129

## 2. Saving Throws

Simulated saving throws against DCs of 5, 10, and 15 using a 1D20, results below:

|              |   DC 5   |  DC 10   |  DC 15   |
| :----------: | :------: | :------: | :------: |
|    Normal    | 0.800463 | 0.549787 | 0.300615 |
|  Advantage   | 0.959989 | 0.798470 | 0.510370 |
| Disadvantage | 0.640447 | 0.302630 | 0.090211 |

## 3. Death Saves

Simulated death saves:

If health drops to 0 or below, roll a d20 each turn:
- <10:	failure
- 10+:	success
- 1:	2 failures
- 20:	gain 1 health, revived

Probability of outcomes:

|   Dead   | Stabilized | Revived  |
| :------: | :--------: | :------: |
| 0.405033 |  0.413459  | 0.181508 |

## Note

All numbers obtained using exactly 1 million iterations
