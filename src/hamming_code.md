# Hamming code
------
## 背景
汉明码通过多次奇偶校验来确定
### 奇校验
> - 对于数据的比特,检查其中1的个数 N.
 - 如果N是奇数为了保证加上校验位后整串比特中1的个数还是奇数. 那么需要将校验位设置为 0
 - 如果N是偶数为了保证加上校验位后整串比特中1的个数是奇数. 那么需要将校验位设置为 1
### 偶校验
> - 对于数据的比特,检查其中1的个数 N.
 - 如果N是偶数为了保证加上校验位后整串比特中1的个数还是偶数. 那么需要将校验位设置为 0
 - 如果N是奇数为了保证加上校验位后整串比特中1的个数是偶数. 那么需要将校验位设置为 1

举例
```
奇校验
1011010[1]
//y: no error; x: error bit
no error
[1][0][1][1][0][1][0][1]  //five 1  No Error detected

one error
[f][t][t][t][t][t][t][t]
[0][0][1][1][0][1][0][1]  //four 1  Error detected
double error
[f][t][t][t][f][t][t][t]
[0][0][1][1][1][1][0][1]  //five 1  No errors detected
three error
[f][t][f][t][f][t][t][t]
[0][0][0][1][1][1][0][1]  //four 1  Error detected
four error (check code error)
[f][t][f][t][f][t][t][f]
[0][0][0][1][1][1][0][0]  //three 1 No errors detected

偶校验
1011010[0]
no error
[1][0][1][1][0][1][0][0]  //four 1  No Error detected

one error
[f][t][t][t][t][t][t][t]
[0][0][1][1][0][1][0][0]  //three 1 Error detected
double error
[f][t][t][t][f][t][t][t]
[0][0][1][1][1][1][0][0]  //four 1  No errors detected
three error
[f][t][f][t][f][t][t][t]
[0][0][0][1][1][1][0][0]  //three 1 Error detected
four error (check code error)
[f][t][f][t][f][t][t][f]
[0][0][0][1][1][1][0][1]  //four 1  No errors detected

//显而易见 奇偶校验只能检查出奇数个比特同时错误 对于偶数个比特同时错误爱莫能助 
```

### 缺点
* 奇偶校验位是一种**错误校验码** 因为不能确定哪一位出错,所以它*不能校正错误*.当发生错误时只能丢弃重传.
### 优点
* 奇偶校验位时使用一位数据能够达到的最好的校验码 并且仅仅需要一些异或门(门电路)就能够生成.

## Main
了解奇偶校验之后,如果一条消息中包含多个用于纠错的bit,且通过精心安置计算这些纠错位使之产生不同的位置出错产生不同的错误结果那样我们就可以找到出错位置了并可以纠正它.
### 校验位的规律可以如下表表示
> <table style="width: 489px;">
<tbody>
<tr>
<td>index</td>
<td></td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>10</td>
<td>11</td>
<td>12</td>
<td>13</td>
<td>14</td>
<td>15</td>
<td>16</td>
<td>17</td>
<td>18</td>
<td>19</td>
<td>20</td>
<td rowspan="7">...</td>
</tr>
<tr>
<td>编码后的数据</td>
<td></td>
<td>p1</td>
<td>p2</td>
<td>d1</td>
<td>p4</td>
<td>d2</td>
<td>d3</td>
<td>d4</td>
<td>p8</td>
<td>d5</td>
<td>d6</td>
<td>d7</td>
<td>d8</td>
<td>d9</td>
<td>d10</td>
<td>d11</td>
<td>p16</td>
<td>d12</td>
<td>d13</td>
<td>d14</td>
<td>d15</td>
</tr>
<tr>
<td rowspan="5">奇偶校验位覆盖率</td>
<td>p1</td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
<td>x</td>
<td></td>
</tr>
<tr>
<td>p2</td>
<td></td>
<td>x</td>
<td>x</td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td></td>
</tr>
<tr>
<td>p4</td>
<td></td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>x</td>
</tr>
<tr>
<td>p8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>p16</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
</tbody>
</table>

> ![HammingCode_1-1.png](https://Kingmeng-Stack.github.io/Blog/image/HammingCode_1-1.png)

### 由表格我们可以如下分析
 * 数据位的位置序号中所有为二的幂次方的位（编号1，2，4，8，等，即数据位位置序号的二进制表示中只有一个1）是校验位
 * 所有其它位置的数据位（数据位位置序号的二进制表示中至少2个是1）是数据位
 * 校验位负责的数据位
  + P1 : 1(11), 3(11), 5(101), 7(111), 9(1001), 11(1011), 13(1101), 15(1111), 17(10001), 19(10011)
  + P2 : 2(10), 3(11), 6(110), 7(111), 10(1010), 11(1011), 14(1110), 15(1111), 18(10010), 19(10011)
  + P4 : 4(100), 5(101), 6(110), 7(111), 12(1100), 13(1101), 14(1110), 15(1111), 20(10100)
  + P8 : 8(1000), 9(1001), 10(1010), 11(1011), 12(1100), 13(1101), 14(1110), 15(1111)
  + P16: 16(10000), 17(10001), 18(10010), 19(10011), 20(10100)
 * 得到第i个校验位是从2^(i-1)位开始 检验2^(i-1)位,跳过2^(i-1)位... 比如p1 检验1 3 5 7 9 跳过 2 4 6 8 p2 检验 2 3 6 7 10 11 14 15 18 19 跳过 4 5 8 9 12 13 16 17
### 检查错误
* 如果所有的奇偶校验位都是正确的 没有错误
* 如果 1 2 8 奇偶校验位显示错误 那么就是 1⊕2⊕8  ==  11  第三位错误了

