import java.awt.*;
import java.util.*;
import java.awt.event.*;
import javax.swing.*;
public class Maze extends JApplet implements ActionListener, KeyListener
{
    static final long serialVersionUID = 1L;
	Image maze3d,direc,end;
	boolean board[][],done,kg,clear;
	int parboard[][];
	int size;
	int title;
	int length;
	int x,y;
	int recur;
	Button solve,newmaze,help;
	Button ul,u,ur,l,right,dl,d,dr;
	TextField dif;
	Font titleFont;
	Random r;
	//CREATORS (init and newMaze)
	public void start()
	{
		maze3d = getImage(getDocumentBase(), "maze3D.gif");
		direc = getImage(getDocumentBase(), "compass.gif");
		end = getImage(getDocumentBase(), "winner.gif");
		showStatus("Enjoy the mazes :-]");
		getContentPane().setLayout(null);
		solve=new Button("Solve");
		newmaze=new Button("New");
		help=new Button("Help");
		dif=new TextField("Difficulty (5-250)");
		newmaze.setBounds(210,3,105,20);
		help.setBounds(325,3,105,20);
		dif.setBounds(210,27,105,20);
		solve.setBounds(325,27,105,20);
		getContentPane().add(solve);
		getContentPane().add(help);
		getContentPane().add(newmaze);
		getContentPane().add(dif);
 		ul=new Button(" ");
 		u=new Button(" ");
 		ur=new Button(" ");
 		l=new Button(" ");
 		right=new Button(" ");
 		dl=new Button(" ");
 		d=new Button(" ");
 		dr=new Button(" ");
 		ul.setBounds(440,3,13,13);
 		l.setBounds(440,18,13,13);
 		dl.setBounds(440,33,13,13);
 		u.setBounds(457,3,13,13);
 		d.setBounds(457,33,13,13);
 		ur.setBounds(474,3,13,13);
 		right.setBounds(474,18,13,13);
 		dr.setBounds(474,33,13,13);
 		ul.addActionListener(this);
 		u.addActionListener(this);
 		ur.addActionListener(this);
 		l.addActionListener(this);
 		right.addActionListener(this);
 		dl.addActionListener(this);
 		d.addActionListener(this);
 		dr.addActionListener(this);
		getContentPane().add(ul);
		getContentPane().add(u);
		getContentPane().add(ur);
		getContentPane().add(l);
		getContentPane().add(right);
		getContentPane().add(dl);
		getContentPane().add(d);
		getContentPane().add(dr);
		solve.addActionListener(this);
		help.addActionListener(this);
		newmaze.addActionListener(this);
		dif.addActionListener(this);
		addKeyListener(this);
		getGraphics().drawImage(maze3d,00,50,this);
	}
	public void init()
	{
		r=new Random();
		showStatus("Enjoy the mazes :-]");
		titleFont=new Font("title",3,45);
		title=50;
		x=1;
		y=1;clear=true;
	}
	public void newMaze()
	{
		showStatus("Please be patient :-]");
		board=new boolean[length][length];
		parboard=new int[length][length];
		for(int cv=0;cv<length;cv++)
		{
			board[0][cv]=true;
			board[length-1-cv][0]=true;
			board[length-1-cv][length-1]=true;
			board[length-1][length-1-cv]=true;
			parboard[0][cv]=1;
			parboard[length-1-cv][0]=1;
			parboard[length-1-cv][length-1]=1;
			parboard[length-1][length-1-cv]=1;
		}
		int Switch=r.nextInt(3);
		for(int cv=0;cv<recur;cv++)
		{
			int x1=r.nextInt(length-2)+1;
			int x2=r.nextInt((length-2)*(length-2));
			x2=(int)Math.sqrt(x2);
			x2++;
			if(Switch==1)
			{
				if(cv<recur/3||cv>(recur/3)*2)
				{
					int temp=x1;
					x1=x2;
					x2=temp;
				}
			}
			if(Switch==2)
			{
				x1=r.nextInt(length-2)+1;
				x2=r.nextInt(length-2)+1;
			}
			int x3=0;
			if(board[x1][x2-1])
			{
				x3++;
			}
			if(board[x1][x2+1])
			{
				x3++;
			}
			if(board[x1+1][x2])
			{
				x3++;
			}
			if(board[x1-1][x2])
			{
				x3++;
			}
			if(x3==1)
			{
				board[x1][x2]=true;
				parboard[x1][x2]=1;
			}
		}
	}
	//DISPLAY METHODS
	public void paint(Graphics g)
	{
		showStatus("Enjoy the mazes :-]");
		g.setFont(titleFont);
		g.drawString("MAZES",5,41);
		g.drawImage(direc,452,12,this);
		g.setFont(new Font("",1,30));
		if(length>4)
		{
			displayMaze(g);
		}
		else
		{
			g.drawImage(maze3d,-10,50,this);
			g.drawString("Enter a difficulty and",50,120);
			g.drawString("click 'New' to begin.",50,155);
		}
	}
	public void help()
	{
    	JOptionPane.showMessageDialog(null,"To begin, type a difficulty into the textbox and click 'New'. \n"+"A maze will appear. \n"+ "The higher the number you enter, the harder the maze will be.\n"+"Use the boxes in the upper-right hand corner of the applet to navigate the maze. \n"+"If you get stuck, click the 'Solve' button for the solution.","                                                          HELP",JOptionPane.INFORMATION_MESSAGE);
  	}
	public void displayMaze(Graphics g)
	{
		if(clear)
		clearMaze(g);
		for(int cv=0;cv<length;cv++)
		{
			for(int cv2=0;cv2<length;cv2++)
			{
				if(board[cv][cv2])
				{
					g.fillOval(cv*size,cv2*size+title,size,size);
				}
			}
		}
		displayStartAndFinish(g);
		clear=true;
		showStatus("Enjoy the mazes :-]");
	}
	public void displayMaze2(Graphics g)
	{
		g.setColor(Color.black);
		clearMaze(g);
		g.setColor(Color.yellow);
		for(int cv=0;cv<length;cv++)
		{
			for(int cv2=0;cv2<length;cv2++)
			{
				if(parboard[cv][cv2]==1)
				{
					g.fillOval(cv*size,cv2*size+title,size,size);
				}
			}
		}
		g.setColor(Color.black);
		for(int cv=0;cv<length;cv++)
		{
			for(int cv2=0;cv2<length;cv2++)
			{
				if(board[cv][cv2])
				{
					g.fillOval(cv*size,cv2*size+title,size,size);
				}
			}
		}
		displayStartAndFinish(g);
	}
	public void displayStartAndFinish(Graphics g)
	{
		g.setColor(Color.green);
		g.fillRect(size,size+title,size,size);
		g.fillRect((length-2)*size,(length-2)*size+title,size,size);
		g.setColor(Color.black);
	}
	public void solve(Graphics g)
	{
		showStatus("Please be patient :-]");
		done=false;
		displayMaze(g);
		x=1;y=1;
		solvePart2(g);
		showStatus("Enjoy the mazes :-]");
	}
	public void solvePart2(Graphics g)
	{
		while(!done)
		{
			showStatus("Please be patient :-]");
			kg=false;
			if(x==length-2&&y==x)
			{
				done=true;
				break;
			}
                        int tx,ty;
			g.setColor(Color.red);
			if(0==parboard[x+1][y+1])
			{
				tx=x;ty=y;
				x++;y++;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			else if(0==parboard[x][y+1])
			{
				tx=x;ty=y;
				y++;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			else if(0==parboard[x+1][y])
			{
				tx=x;ty=y;
				x++;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			else if((0==parboard[x-1][y+1]))
			{
				tx=x;ty=y;
				x--;y++;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			else if(0==parboard[x+1][y-1])
			{
				tx=x;ty=y;
				x++;y--;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			else if(0==parboard[x-1][y])
			{
				tx=x;ty=y;
				x--;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			else if(0==parboard[x][y-1])
			{
				tx=x;ty=y;
				y--;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			else if(0==parboard[x-1][y-1])
			{
				tx=x;ty=y;
				x--;y--;
				g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
				parboard[tx][ty]=2;
				if(x==length-2&&y==x)
				{
					clear=false;
					g.setColor(Color.black);
					displayMaze(g);
					done=true;
					break;
				}
				kg=true;
			}
			if(!kg)
			{
				parboard[x][y]=1;
				x=1;y=1;
				for(int cv=0;cv<length;cv++)
				{
					for(int cv2=0;cv2<length;cv2++)
					{
						if(parboard[cv][cv2]==2)
						{
							parboard[cv][cv2]=0;
						}
					}
				}
				if(done)
				{
					break;
				}
				clearMaze(g);
			}
		}
	}
	public void clearMaze(Graphics g)
	{
		g.setColor(Color.white);
		g.fillRect(0,title,500,500);
		g.setColor(Color.black);
	}
	//LISTENERS
	public void keyTyped(KeyEvent e)
	{
           Graphics g=getGraphics();
           g.setColor(Color.red);
           if(e.getKeyChar()=='1')
           {
              dl(g);
           }
           if(e.getKeyChar()=='2')
           {
              d(g);
           }
           if(e.getKeyChar()=='3')
           {
              dr(g);
           }
           if(e.getKeyChar()=='4')
           {
              l(g);
           }
           if(e.getKeyChar()=='6')
           {
              r(g);
           }
           if(e.getKeyChar()=='7')
           {
              ul(g);
           }
           if(e.getKeyChar()=='8')
           {
              u(g);
           }
           if(e.getKeyChar()=='9')
           {
              ur(g);
           }
           g.setColor(Color.black);
	}
        public void keyReleased(KeyEvent e)
	{
	}
	public void keyPressed(KeyEvent e)
	{
	}
	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource()==dif)
		{
			e.setSource(newmaze);
		}
		Graphics g=getGraphics();
		if(e.getSource()==newmaze)
		{
			try
			{
				int temp=length;
				String s=(dif.getText()).trim();
				double d=(new Double(s.trim())).doubleValue();
				length=(int)d;
				if(length>4&&length<251&&(!s.equals("")))
				{
					size=500/length;
					recur=(length)*(length)*(length);
					init();
					newMaze();
					displayMaze(g);
				}
				else
				{
					length=temp;
					JOptionPane.showMessageDialog(null,"You must enter a number between 5 and 250 inclusive.","DIFFICULTY",JOptionPane.WARNING_MESSAGE);
				}
			}
			catch(Throwable ioe)
			{
				JOptionPane.showMessageDialog(null,"You must enter a number between 5 and 250 inclusive.","DIFFICULTY",JOptionPane.WARNING_MESSAGE);
			}
		}
		if(e.getSource()==solve)
		{
			solve(g);
		}
		if(e.getSource()==help)
		{
		}
		g.setColor(Color.red);
		if(e.getSource()==ul)
		{
			ul(g);
		}
		if(e.getSource()==l)
		{
			l(g);
		}
		if(e.getSource()==dl)
		{
			dl(g);
		}
		if(e.getSource()==u)
		{
			u(g);
		}
		if(e.getSource()==d)
		{
			d(g);
		}
		if(e.getSource()==ur)
		{
			ur(g);
		}
		if(e.getSource()==right)
		{
			r(g);
		}
		if(e.getSource()==dr)
		{
			dr(g);
		}
		g.setColor(Color.black);
		if(e.getSource()==help)
		{
			help();
		}
	}
	//MOVEMENT
	public void dl(Graphics g)
	{
		if(!board[x-1][y+1])
		{
			int tx=x,ty=y;
			x--;y++;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,00,50,this);
			}
		}
	}
	public void d(Graphics g)
	{
		if(!board[x][y+1])
		{
			int tx=x,ty=y;
			y++;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,0,50,this);
			}
		}
	}
	public void dr(Graphics g)
	{
		if(!board[x+1][y+1])
		{
			int tx=x,ty=y;
			x++;y++;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,0,50,this);
			}
		}
	}
	public void l(Graphics g)
	{
		if(!board[x-1][y])
		{
			int tx=x,ty=y;
			x--;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,00,50,this);
			}
		}
	}
	public void r(Graphics g)
	{
		if(!board[x+1][y])
		{
			int tx=x,ty=y;
			x++;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,00,50,this);
			}
		}
	}
	public void ul(Graphics g)
	{
		if(!board[x-1][y-1])
		{
			int tx=x,ty=y;
			x--;y--;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,00,50,this);
			}
		}
	}
	public void u(Graphics g)
	{
		if(!board[x][y-1])
		{
			int tx=x,ty=y;
			y--;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,00,50,this);
			}
		}
	}
	public void ur(Graphics g)
	{
		if(!board[x+1][y-1])
		{
			int tx=x,ty=y;
			x++;y--;
			g.drawLine(x*size+((int)(size/2)),y*size+title+((int)(size/2)),tx*size+((int)(size/2)),ty*size+((int)(size/2))+title);
			if(x==length-2&&x==y)
			{
				g.drawImage(end,00,50,this);
			}
		}
	}
}