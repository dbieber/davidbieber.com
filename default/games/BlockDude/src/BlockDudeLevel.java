import java.awt.*;
import java.util.*;
public class BlockDudeLevel
{
	String [][] originalLevel,level;
	int xSize,ySize,startX=-1,startY=-1;
	boolean isHoldingBlock;
	BlockDude blockDude;
	Color rand;
	public BlockDudeLevel(LevelMaker l,BlockDude bldd)
	{
		Random r=new Random();
		rand=new Color(r.nextInt(255),r.nextInt(255),r.nextInt(255));
		blockDude=bldd;
		isHoldingBlock=false;
		xSize=l.readInt();
		ySize=l.readInt();
		String line;
		originalLevel=new String[xSize][ySize];
		int cvy=0;
		while(cvy<ySize)
		{
			line=l.readLine();
			int cvx=0;
			while(cvx<line.length())
			{
				originalLevel[cvx][cvy]=line.substring(cvx,cvx+1);
				if(originalLevel[cvx][cvy].equals("L")||originalLevel[cvx][cvy].equals("R"))
				{
					startX=cvx;
					startY=cvy;
				}
				cvx++;
			}
			cvy++;
		}
		level=originalLevel;
	}
	public void restart()
	{
		level=originalLevel;
	}
	public String toString()
	{
		String st="";
		for(int cv=0;cv<ySize;cv++)
		{
			for(int cv2=0;cv2<xSize;cv2++)
			{
				st+=level[cv2][cv];
			}	
			st+="\n";
		}
		return st;
	}
	public void display()
	{
		Graphics temp = blockDude.g;
		if(blockDude.getImageStyle().equals("3D"))
		{
			temp.setColor(rand);
			temp.fillRect(0,24,1200,1000);
		}
		for(int cv=ySize-1;cv>=0;cv--)
		{
			for(int cv2=0;cv2<xSize;cv2++)
			{
				temp.drawImage(blockDude.getImage(level[cv2][cv]),cv2*24+1,cv*24+24,blockDude);
			}
		}
		if(!blockDude.getImageStyle().equals("3D"))
		{	temp.setColor(rand);
			temp.fillRect((xSize)*24+1,24,2000,2000);
			temp.fillRect(0,(ySize+1)*24,2000,2000);
		}
	}
	public void left()
	{
		if(!isHoldingBlock)
		{
			level[startX][startY]="L";
			if(level[startX-1][startY].equals("G"))
			{
				onWin();
				return;
			}
			if(level[startX-1][startY].equals("o"))
			{
				return;
			}
			if(level[startX-1][startY].equals("x"))
			{
				return;
			}
			level[startX-1][startY]="L";
			level[startX][startY]=" ";
			startX--;
			blockDudeFall();
		}
		else
		{
			level[startX][startY]="L";
			if(level[startX-1][startY].equals("G"))
			{
				onWin();
				return;
			}
			if(level[startX-1][startY].equals("o"))
			{
				return;
			}
			if(level[startX-1][startY].equals("x"))
			{
				return;
			}
			level[startX-1][startY]="L";
			level[startX][startY]=" ";
			int blockX,blockY;
			if(level[startX-1][startY-1].equals(" "))
			{
				level[startX-1][startY-1]="o";
				blockX=startX-1;
				blockY=startY-1;
				level[startX][startY-1]=" ";
			}
			else
			{
				isHoldingBlock=false;
				blockX=startX;
				blockY=startY-1;
			}
			level[startX][startY]=" ";
			startX--;
			blockDudeFall();
			fall(blockX,blockY);
		}
	}
	public void fall(int x,int y)
	{
		if(level[x][y].equals("o")&&level[x][y+1].equals(" "))
		{
			level[x][y+1]="o";
			level[x][y]=" ";
			fall(x,y+1);
		}
	}
	public void right()
	{
		if(!isHoldingBlock)
		{
			level[startX][startY]="R";
			if(level[startX+1][startY].equals("G"))
			{
				onWin();
				return;
			}
			if(level[startX+1][startY].equals("o"))
			{
				return;
			}
			if(level[startX+1][startY].equals("x"))
			{
				return;
			}
			level[startX+1][startY]="R";
			level[startX][startY]=" ";
			startX++;
			blockDudeFall();
		}
		else
		{
			level[startX][startY]="R";
			if(level[startX+1][startY].equals("G"))
			{
				onWin();
				return;
			}
			if(level[startX+1][startY].equals("o"))
			{
				return;
			}
			if(level[startX+1][startY].equals("x"))
			{
				return;
			}
			level[startX+1][startY]="R";
			level[startX][startY]=" ";
			int blockX,blockY;
			if(level[startX+1][startY-1].equals(" "))
			{
				level[startX+1][startY-1]="o";
				blockX=startX+1;
				blockY=startY-1;
				level[startX][startY-1]=" ";
			}
			else
			{
				isHoldingBlock=false;
				blockX=startX;
				blockY=startY-1;
			}
			level[startX][startY]=" ";
			startX++;
			blockDudeFall();
			fall(blockX,blockY);
		}
	}
	public void up()
	{
		if(!isHoldingBlock)
		{
			if(!level[startX][startY-1].equals(" "))
			{
				return;
			}
			if(level[startX][startY].equals("R"))
			{
				if(level[startX+1][startY-1].equals("G"))
				{
					onWin();
					return;
				}
				if(level[startX+1][startY].equals("x")||level[startX+1][startY].equals("o"))
				{
					if(level[startX+1][startY-1].equals(" "))
					{
						level[startX+1][startY-1]="R";
						level[startX][startY]=" ";
						startX++;
						startY--;
					}
				}
			}
			else
			{
				if(level[startX-1][startY-1].equals("G"))
				{
					onWin();
					return;
				}
				if(level[startX-1][startY].equals("x")||level[startX-1][startY].equals("o"))
				{
					if(level[startX-1][startY-1].equals(" "))
					{
						level[startX-1][startY-1]="L";
						level[startX][startY]=" ";
						startX--;
						startY--;
					}
				}
			}
		}
		else //if(!isHoldingBlock)
		{
			if(!level[startX][startY-2].equals(" "))
			{
				return;
			}
			if(level[startX][startY].equals("R"))
			{
				if(level[startX+1][startY].equals("x")||level[startX+1][startY].equals("o"))
				{
					if(level[startX+1][startY-1].equals(" "))
					{
						level[startX+1][startY-1]="R";
						level[startX][startY]=" ";
						if(level[startX+1][startY-2].equals(" "))//not entered
						{
							level[startX+1][startY-2]="o";
							level[startX][startY-1]=" ";
						}
						else
						{
							isHoldingBlock=false;
							fall(startX,startY-1);
						}
						startX++;
						startY--;
					}
				}
			}
			else
			{
				if(level[startX-1][startY].equals("x")||level[startX-1][startY].equals("o"))
				{
					if(level[startX-1][startY-1].equals(" "))
					{
						level[startX-1][startY-1]="L";
						level[startX][startY]=" ";
						if(level[startX-1][startY-2].equals(" "))
						{
							level[startX-1][startY-2]="o";
							level[startX][startY-1]=" ";
						}
						else
						{
							isHoldingBlock=false;
							fall(startX,startY-1);
						}
						startX--;
						startY--;
					}
				}
			}
		}
	}
	public void liftOrDrop()
	{
		if(isHoldingBlock)
		{
			if(level[startX][startY].equals("L"))
			{
				if(level[startX-1][startY-1].equals(" "))
				{
					isHoldingBlock=false;
					level[startX-1][startY-1]="o";
					level[startX][startY-1]=" ";
					fall(startX-1,startY-1);
					return;
				}
				else
				{
					return;
				}
			}
			else
			{
				if(level[startX+1][startY-1].equals(" "))
				{
					isHoldingBlock=false;
					level[startX+1][startY-1]="o";
					level[startX][startY-1]=" ";
					fall(startX+1,startY-1);
					return;
				}
				else
				{
					return;
				}
			}
		}
		else
		{
			if(level[startX][startY].equals("L"))
			{
				if(level[startX-1][startY].equals("o")&&level[startX-1][startY-1].equals(" ")&&level[startX][startY-1].equals(" "))
				{
					level[startX-1][startY]=" ";
					level[startX][startY-1]="o";
					isHoldingBlock=true;
				}
				else
				{
					return;
				}
			}
			else
			{
				if(level[startX+1][startY].equals("o")&&level[startX+1][startY-1].equals(" ")&&level[startX][startY-1].equals(" "))
				{
					level[startX+1][startY]=" ";
					level[startX][startY-1]="o";
					isHoldingBlock=true;
				}
				else
				{
					return;
				}
			}
		}
	}
	public void blockDudeFall()
	{
		if(level[startX][startY+1].equals("G"))
		{
			onWin();
			return;
		}
		if(level[startX][startY+1].equals(" "))
		{
			level[startX][startY+1]=level[startX][startY];
			level[startX][startY]=" ";
			startY++;
			blockDudeFall();
		}
		
	}
	public void onWin()
	{
		blockDude.levelUp();
	}
}