/*
   JOptionPane.showMessageDialog(null,"Copy and paste the contents of the textbox into notpad and save the file\nas a valid '.level' file in the levels folder of BlockDude.","Creating a Level",JOptionPane.INFORMATION_MESSAGE);
*/
public class LevelMaker
{
 int num1,num2,line2Return=0;
 boolean return1=true;
 String[] lines;
 boolean isBad=true;
 public LevelMaker(String levelName)
 {
  isBad=false;
  if(levelName.equals("beginner1.level"))
  {
   num1=10;
   num2=3;
   lines=new String[num2];
   lines[0] ="xxxxxxxxxx";
   lines[1] ="xR      Gx";
   lines[2] ="xxxxxxxxxx";
  }
  else if(levelName.equals("beginner2.level"))
  {
   num1=10;
   num2=3;
   lines=new String[num2];
   lines[0] ="xxxxxxxxxx";
   lines[1] ="xG      Lx";
   lines[2] ="xxxxxxxxxx";
  }
  else if(levelName.equals("beginner3.level"))
  {
   num1=10;
   num2=6;
   lines=new String[num2];
   lines[0] ="xxxxxxxxxx";
   lines[1] ="x        x";
   lines[2] ="x      x x";
   lines[3] ="x     xx x";
   lines[4] ="xRx  xxxGx";
   lines[5] ="xxxxxxxxxx";
  }
  else if(levelName.equals("beginner4.level"))
  {
   num1=10;
   num2=5;
   lines=new String[num2];
   lines[0] ="xxxxxxxxxx";
   lines[1] ="x        x";
   lines[2] ="x     x  x";
   lines[3] ="xRo   x Gx";
   lines[4] ="xxxxxxxxxx";
  }
  else if(levelName.equals("beginner5.level"))
  {
   num1=10;
   num2=7;
   lines=new String[num2];
   lines[0] ="    xxxxxx";
   lines[1] ="   x    Gx";
   lines[2] ="  x     xx";
   lines[3] =" x      x ";
   lines[4] ="x       x ";
   lines[5] ="xRoooooox ";
   lines[6] ="xxxxxxxxx ";
  }
  else if(levelName.equals("beginner6.level"))
  {
   num1=14;
   num2=7;
   lines=new String[num2];
   lines[0] ="o            x";
   lines[1] ="o            x";
   lines[2] ="o      o     x";
   lines[3] ="o  G  o      x";
   lines[4] ="o    o       x";
   lines[5] ="xRo          x";
   lines[6] ="xxxxxxxxxxxxxx";
  }
  else if(levelName.equals("beginner7.level"))
  {
   num1=26;
   num2=15;
   lines=new String[num2];
   lines[0] ="xxxxxxxxxxxxxxxxxxxxxxxxxx";
   lines[1] ="xR                       x";
   lines[2] ="xxxxxxxxxxxxxxxxxxxxxxxx x";
   lines[3] ="x                        x";
   lines[4] ="x xxxxxxxxxxxxxxxxxxxxxxxx";
   lines[5] ="x                        x";
   lines[6] ="xxxxxxxxxxxxxxxxxxxxxxxx x";
   lines[7] ="x                        x";
   lines[8] ="x                     xxxx";
   lines[9] ="x x   x   x   x   x      x";
   lines[10]="x x   x   x   x   x ooooox";
   lines[11]="x xxxxxxxxxxxxxxxxxxxxxxxx";
   lines[12]="x                        x";
   lines[13]="xxxxxxxxxxxxxxxxxxxxxxxxGx";
   lines[14]="                       xxx";
  }
  else if(levelName.equals("original1.level"))
  {
   num1=20;
   num2=7;
   lines=new String[num2];
   lines[0]="x                  x";
   lines[1]="x                  x";
   lines[2]="x                  x";
   lines[3]="x                  x";
   lines[4]="x   x       x      x";
   lines[5]="xG  x   x o x o R  x";
   lines[6]="xxxxxxxxxxxxxxxxxxxx";
  }
  else if(levelName.equals("original2.level"))
  {
   num1=22;
   num2=10;
   lines=new String[num2];
   lines[0]=" x    xx        xx    ";
   lines[1]=" x                x   ";
   lines[2]="xx                 x  ";
   lines[3]="xG                  x ";
   lines[4]="xx                   x";
   lines[5]=" x           x  o    x";
   lines[6]=" x           xo oo R x";
   lines[7]=" xxxxx   xxxxxxxxxxxxx";
   lines[8]="     x  ox            ";
   lines[9]="     xxxxx            ";
  }
  else if(levelName.equals("original3.level"))
  {
   num1=19;
   num2=11;
   lines=new String[num2];
   lines[0]=" x                 ";
   lines[1]=" x   xxxxxxxxxxxxx ";
   lines[2]="x x x             x";
   lines[3]="x  x              x";
   lines[4]="x                ox";
   lines[5]="x               oox";
   lines[6]="x xxx    L   xo xx ";
   lines[7]="x x x    x  xxxxx  ";
   lines[8]="x x xoo xx  x      ";
   lines[9]="xGx xxxxxx xx      ";
   lines[10]="xxx xx   xxx       ";
  }
  else if(levelName.equals("original4.level"))
  {
   num1=24;
   num2=16;
   lines=new String[num2];
   lines[0]= "                  x     ";
   lines[1]= "                 x x    ";
   lines[2]= "       x        x   x   ";
   lines[3]= "      x x      x     x  ";
   lines[4]= "   xxx   x    x       x ";
   lines[5]= "  x       x  x         x";
   lines[6]= " x         xx          x";
   lines[7]= " x                    ox";
   lines[8]= " x                   oox";
   lines[9]= " x               L   xxx";
   lines[10]="xx    x          x   x  ";
   lines[11]="xG    x o        xxxxx  ";
   lines[12]="xxxxx x o   o  xxx      ";
   lines[13]="    x x o x xo x        ";
   lines[14]="    x xxxxxxxxxx        ";
   lines[15]="    xxx                 ";
  }
  else if(levelName.equals("original5.level"))
  {
   num1=22;
   num2=14;
   lines=new String[num2];
   lines[0]= "     xxx    xxxxxxxxx ";
   lines[1]= " xxxx   xxxx         x";
   lines[2]= "x                    x";
   lines[3]= "x                    x";
   lines[4]= "x                    x";
   lines[5]= "x     x              x";
   lines[6]= "x     x              x";
   lines[7]= "x     xoooo          x";
   lines[8]= "xG   xxxxxxxL        x";
   lines[9]= "xx xxx     xx x     ox";
   lines[10]=" x x        x xx   oox";
   lines[11]=" x x        x xx  ooox";
   lines[12]=" xxx        x xxxxxxxx";
   lines[13]="            xxx       ";
  }
  else if(levelName.equals("original6.level"))
  {
   num1=21;
   num2=13;
   lines=new String[num2];
   lines[0]= " xxx             xxxx";
   lines[1]= " x  xxxxxxxxxxxxx   x";
   lines[2]= "xx                  x";
   lines[3]= "xG                  x";
   lines[4]= "xx                  x";
   lines[5]= " x                oox";
   lines[6]= " xoo        x  o  xxx";
   lines[7]= " xooo       xLooo x  ";
   lines[8]= " xoooo      xxxxx x  ";
   lines[9]= " xxxxx    xxx   xxx  ";
   lines[10]="     x   ox          ";
   lines[11]="     xx xxx          ";
   lines[12]="      xxx            ";
  }
  else if(levelName.equals("original7.level"))
  {
   num1=24;
   num2=14;
   lines=new String[num2];
   lines[0]= "  x   xxxxx   xx   xxx  ";
   lines[1]= " x x x     x x  x x   x ";
   lines[2]= " x  xx      xx   xx    x";
   lines[3]= " x   x       x    x    x";
   lines[4]= " x                    ox";
   lines[5]= " x                    ox";
   lines[6]= "xx                   oox";
   lines[7]= "xG   o               xxx";
   lines[8]= "xx   x o     x    xx x  ";
   lines[9]= " x   x o    xx o Lxxxx  ";
   lines[10]=" xx  x ooo  xx ooox     ";
   lines[11]="  x  xxxxxx xxxxxxx     ";
   lines[12]="  xx x    xxx           ";
   lines[13]="   xxx                  ";
  }
  else if(levelName.equals("original8.level"))
  {
   num1=27;
   num2=17;
   lines=new String[num2];
   lines[0]=" xxx       xxxx   xxxxxxx  ";
   lines[1]= "x   x     x    x x       x ";
   lines[2]= "x    x   x     xx         x";
   lines[3]= "xo    xxx    x x     xxx  x";
   lines[4]= "xoo         xx      xx x  x";
   lines[5]= "xxxx       xx          xG x";
   lines[6]= "   xx            xx    xx x";
   lines[7]= "  x    o x      x  x      x";
   lines[8]= "  x    ox x    x   x      x";
   lines[9]= " x   xxx   x    x  x     ox";
   lines[10]=" x      x x      xx     oox";
   lines[11]="x        x           xxxxxx";
   lines[12]="x            o            x";
   lines[13]="x    o      xxx          ox";
   lines[14]="x   xxx                 oox";
   lines[15]="x        o       o  L  ooox";
   lines[16]="xxxxxxxxxxxxxxxxxxxxxxxxxxx";
  }
  else if(levelName.equals("original9.level"))
  {
   num1=20;
   num2=16;
   lines=new String[num2];
   lines[0]= "        xxx         ";
   lines[1]= "       x   x        ";
   lines[2]= "      x     x  xxxxx";
   lines[3]= "     x       xx    x";
   lines[4]= "    x     o        x";
   lines[5]= "   x      oo      ox";
   lines[6]= "  x       xxx    oox";
   lines[7]= " x            L xxxx";
   lines[8]= "x             o    x";
   lines[9]= "xG           xxx   x";
   lines[10]="xx    xx   x      ox";
   lines[11]=" x    xxo  xx   xxxx";
   lines[12]=" x    xxxxxxx  xx   ";
   lines[13]=" xxx  x     x xx    ";
   lines[14]="   x xx     xxx     ";
   lines[15]="   xxx              ";
  }
  else if(levelName.equals("original10.level"))
  {
   num1=27;
   num2=19;
   lines=new String[num2];
   lines[0]= "   xxxxxxxxxxxxxxxxxxxxx   ";
   lines[1]= " xx           x         x  ";
   lines[2]= "xxxxo       ooxo   ooo oxx ";
   lines[3]= "x  xx  x   xxxxx  oxxx xx x";
   lines[4]= "x   x  xx        xxx xxx  x";
   lines[5]= "x   xx  xxoooo            x";
   lines[6]= "xG       xxxxxxx          x";
   lines[7]= "xx        x   xxx        xx";
   lines[8]= " x     o   x x  xx        x";
   lines[9]= " x     x    x    xx       x";
   lines[10]=" xxxx  xx             xxxxx";
   lines[11]="   xxxxx      L           x";
   lines[12]="   x          x           x";
   lines[13]="   x         xx    xxxxxxxx";
   lines[14]="   x        xx           x ";
   lines[15]="   x          o         ox ";
   lines[16]="   xo    xxxxxxxxxxx   oox ";
   lines[17]="   xoo  xx         xx ooox ";
   lines[18]="   xxxxxx           xxxxxx ";
  }
  else if(levelName.equals("original11.level"))
  {
   num1=29;
   num2=19;
   lines=new String[num2];
   lines[0]= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
   lines[1]= "x  x   x                    x";
   lines[2]= "x     oxoo            xxxxx x";
   lines[3]= "xo   xxx oxx     o  xx  G x x";
   lines[4]= "xoo    x     L  o       x x x";
   lines[5]= "xxx  oox     x o          x x";
   lines[6]= "x   xxxx      x  xxx   xxx  x";
   lines[7]= "xo            x x      x  o x";
   lines[8]= "xoo       xxx x xo    x  xxxx";
   lines[9]= "xxxx o   xxx  x xxo  x o x  x";
   lines[10]="x           o xxx  ox   x   x";
   lines[11]="x   o     oo x   xxxx       x";
   lines[12]="x    xxxxxxxxx        xxxxx x";
   lines[13]="x              o   oxx    x x";
   lines[14]="xxxx           o   x    oox x";
   lines[15]="xoxx   x    x          xxxx x";
   lines[16]="xxoxxx x    x   ooo o       x";
   lines[17]="xoxoxoxx    x        ooo    x";
   lines[18]="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
  }
  else if(levelName.equals("other1.level"))
  {
   num1=24;
   num2=18;
   lines=new String[num2];
   lines[0]="xxxxxxxxxxxxxxxxxxxxxxxx";
   lines[1]="x                     Lx";
   lines[2]="x  x    ox    o   oxxxxx";
   lines[3]="x  ox  oxox  ox  oxxoooo";
   lines[4]="x   oxox  oxox  oxxooxxx";
   lines[5]="x  x ox ox ox o xxooxooo";
   lines[6]="x  ox  oxox  ox oxxooxxx";
   lines[7]="x   oxox  oxox   oxxoooo";
   lines[8]="x    ox    ox     oxxxxx";
   lines[9]="x                     Gx";
   lines[10]="x                      x";
   lines[11]="x o                    x";
   lines[12]="x  o     o     o       x";
   lines[13]="x   o   o o   o       xx";
   lines[14]="x    o o   o o        x ";
   lines[15]="x     o     o     oooox ";
   lines[16]="x                     x ";
   lines[17]="xxxxxxxxxxxxxxxxxxxxxxx ";
  }
  else if(levelName.equals("other2.level"))
  {
   num1=30;
   num2=18;
   lines=new String[num2];
   lines[0]="oxoxoxoxoxoxoxox            Gx";
   lines[1]="xoxoxoxoxoxoxox           xxxx";
   lines[2]="oxoxoxoxoxoxox               x";
   lines[3]="xoxoxoxoxoxox       xxxxxx   x";
   lines[4]="oxoxoxoxoxox                 x";
   lines[5]="xoxoxoxoxox       oooo       x";
   lines[6]="oxoxoxoxox    xxxxxxxx       x";
   lines[7]="xoxoxoxox    x               x";
   lines[8]="oxoxoxox o                   x";
   lines[9]="xoxoxox  xxxxx xxxx          x";
   lines[10]="oxoxox            x        oox";
   lines[11]="xoxox             x       ooox";
   lines[12]="oxox              x      oooox";
   lines[13]="xox      ooooo          ooooox";
   lines[14]="ox      oooooo         oooooxx";
   lines[15]="x      ooooooo xxxxx  oxxxxxx ";
   lines[16]="xR  oooxxxxxxxxx   x oxx      ";
   lines[17]="xxxxxxxx           xxxx       ";
  }
  else if(levelName.equals("other3.level"))
  {
   num1=20;
   num2=11;
   lines=new String[num2];
   lines[0]="       xxxxxxxx  x  ";
   lines[1]=" xxxxxxG       xx x ";
   lines[2]="x      x   oo     x ";
   lines[3]="x      x xxxxxx    x";
   lines[4]="xR             x   x";
   lines[5]="xooo    x         x ";
   lines[6]="xooooo           x  ";
   lines[7]="xxxxxxx    xxxx x   ";
   lines[8]="      x    x  x x   ";
   lines[9]="      x    x   x    ";
   lines[10]="       xxxx         ";
  }
  else if(levelName.equals("other4.level"))
  {
   num1=26;
   num2=15;
   lines=new String[num2];
   lines[0]="xxxxxxxxxxxxxxxxxxxxxxxxxx";
   lines[1]="xR                       x";
   lines[2]="xxxxxxx xxxxx xxxx xxxxx x";
   lines[3]="x      o                 x";
   lines[4]="x xxxxxxxxx xxxxxxxx xxx x";
   lines[5]="x          x             x";
   lines[6]="xx            xx    x    x";
   lines[7]="x                        x";
   lines[8]="x x    x    x    x    ooox";
   lines[9]="x x    x    x    x   oooox";
   lines[10]="x x    x    x    x  ooooox";
   lines[11]="x xxxxxxxxxxxxxxxxxxxxxxxx";
   lines[12]="x                        x";
   lines[13]="xxxxxxxxxxxxxxxxxxxxxxxxGx";
   lines[14]="                       xxx";
  }
  else if(levelName.equals("other5.level"))
  {
    num1=37;
    num2=21;
    lines=new String[num2];
    lines[0]="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    lines[1]="x   R                               x";
    lines[2]="x o o  x  xx  xx  x x               x";
    lines[3]="x o o x x x x x x x x               x";
    lines[4]="x ooo xxx xx  xx  x x               x";
    lines[5]="x o o x x x   x    x                x";
    lines[6]="x o o x x x   x    x                x";
    lines[7]="x                                   x";
    lines[8]="x   oo  xxx xx  xxx x x xx   x  x x x";
    lines[9]="x   o o  x  x x  x  x x x x x x x x x";
    lines[10]="x   oo   x  xx   x  xxx x x xxx x x x";
    lines[11]="x   o o  x  x x  x  x x x x x x  x  x";
    lines[12]="x   oo  xxx x x  x  x x xx  x x  x  x";
    lines[13]="x                                   x";
    lines[14]="x       oo  xxx  xx  x  x   xxx x   x";
    lines[15]="x       o o  x  x   x x x   x   x   x";
    lines[16]="x       o o  x  x   x x x   xxx x   x";
    lines[17]="x       o o  x  x   x x x   x   G   x";
    lines[18]="x       o o xxx  xx  x  xxx xxx x   x";
    lines[19]="x                                   x";
    lines[20]="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
  }
  else if(levelName.equals("expert1.level"))
  {
    num1=21;
    num2=15;
    lines=new String[num2];
    lines[0]="     x x x  x        ";
    lines[1]="    x  x x  x        ";
    lines[2]="  xx   x x  x        ";
    lines[3]=" x     x    x        ";
    lines[4]="x           x        ";
    lines[5]="x        o  x        ";
    lines[6]="x       ooo          ";
    lines[7]=" x     R             ";
    lines[8]=" xo    xxxx  ooo     ";
    lines[9]="  xx      xx ooo     ";
    lines[10]="    xxo     xG o     ";
    lines[11]="      xo     xxxx   x";
    lines[12]="       xo          ox";
    lines[13]="        xo         x ";
    lines[14]="         xxxxxxxxxx  ";
  }
  else
  {
    isBad=true;
    if(levelName.equals("WIN.level"))
    {
      isBad=false;
    }
    num1=42;
    num2=23;
    lines=new String[num2];
    lines[0] ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    lines[1] ="x                   R                    x";
    lines[2] ="x    o       o    ooooo   o         o    x";
    lines[3] ="x     o     o    o     o  o         o    x";
    lines[4] ="x      o   o    o       o o         o    x";
    lines[5] ="x       o o     o       o o         o    x";
    lines[6] ="x        o      o       o o         o    x";
    lines[7] ="x        o      o       o o         o    x";
    lines[8] ="x        o      o       o  o       o     x";
    lines[9] ="x        o       o     o    o     o      x";
    lines[10]="x        o        ooooo      ooooo       x";
    lines[11]="x                                        x";
    lines[12]="x o             o ooooooooooo  o       o x";
    lines[13]="x o             o G    o       oo      o x";
    lines[14]="x o             o      o       o o     o x";
    lines[15]="x o             o     Go       o  o    o x";
    lines[16]="x o             o      o       o   o   o x";
    lines[17]="x  o     o     o       o       o    o  o x";
    lines[18]="x   o   o o   o        o       o     o o x";
    lines[19]="x    o o   o o         o       o      oo x";
    lines[20]="x     o     o     ooooooooooo  o       o x";
    lines[21]="x                                        x";
    lines[22]="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
  }
 }
 public int readInt()
 {
   if(return1)
   {
     return1=false;
     return num1;
   }
   return num2;
 }
 public String readLine()
 {
   line2Return++;
   return lines[line2Return-1];
 }
 public boolean bad()
 {
   return isBad;
 }
}