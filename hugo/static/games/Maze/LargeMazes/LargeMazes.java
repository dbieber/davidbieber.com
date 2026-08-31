import java.awt.*;
import java.applet.*;
import java.util.*;
import java.awt.event.*;
import javax.swing.*;
public class LargeMazes extends JApplet implements ActionListener, KeyListener
{
	Image maze3d,direc,end;
	boolean board[][],done,kg,clear;
	final int horizbigness=1100;
	final int vertibigness=600;
	int parboard[][];
	int hsize,vsize,size;
	int title;
	int lengthX,lengthY;
	int x,y;
	int recur;
	Button solve,newmaze,help;
	Button ul,u,ur,l,right,dl,d,dr;
	TextField difX,difY;
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
		difX=new TextField("X");
		difY=new TextField("Y");
		newmaze.setBounds(210,3,105,20);
		help.setBounds(325,3,105,20);
		difX.setBounds(210,27,50,20);
		difY.setBounds(263,27,50,20);
		solve.setBounds(325,27,105,20);
		getContentPane().add(solve);
		getContentPane().add(help);
		getContentPane().add(newmaze);
		getContentPane().add(difX);
		getContentPane().add(difY);
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
		difX.addActionListener(this);
		difY.addActionListener(this);
		addKeyListener(this);
		getGraphics().drawImage(end,00,50,this);
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
		board=new boolean[lengthX][lengthY];
		parboard=new int[lengthX][lengthY];
		for(int cv=0;cv<Math.max(lengthX,lengthY);cv++)//////
		{
			try{board[0][cv]=true;}catch(Exception e){}
			try{board[lengthX-1-cv][0]=true;}catch(Exception e){}
			try{board[lengthX-1-cv][lengthY-1]=true;}catch(Exception e){}
			try{board[lengthX-1][lengthY-1-cv]=true;}catch(Exception e){}
			try{parboard[0][cv]=1;}catch(Exception e){}
			try{parboard[lengthX-1-cv][0]=1;}catch(Exception e){}
			try{parboard[lengthX-1-cv][lengthY-1]=1;}catch(Exception e){}
			try{parboard[lengthX-1][lengthY-1-cv]=1;}catch(Exception e){}
		}
		int Switch=r.nextInt(3);
		for(int cv=0;cv<recur;cv++)
		{
			int x1=r.nextInt(lengthX-2)+1;
			int x2=r.nextInt((lengthY-2)*(lengthY-2));
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
				x1=r.nextInt(lengthX-2)+1;
				x2=r.nextInt(lengthY-2)+1;
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
		if(lengthX>1&&lengthY>1)
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
		for(int cv=0;cv<lengthX;cv++)
		{
			for(int cv2=0;cv2<lengthY;cv2++)
			{
				if(board[cv][cv2])
				{
					g.fillOval(cv*hsize,cv2*vsize+title,hsize,vsize);
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
		for(int cv=0;cv<lengthX;cv++)
		{
			for(int cv2=0;cv2<lengthY;cv2++)
			{
				if(parboard[cv][cv2]==1)
				{
					g.fillOval(cv*hsize,cv2*vsize+title,hsize,vsize);
				}
			}
		}
		g.setColor(Color.black);
		for(int cv=0;cv<lengthX;cv++)
		{
			for(int cv2=0;cv2<lengthY;cv2++)
			{
				if(board[cv][cv2])
				{
					g.fillOval(cv*hsize,cv2*vsize+title,hsize,vsize);
				}
			}
		}
		displayStartAndFinish(g);
	}
	public void displayStartAndFinish(Graphics g)
	{
		g.setColor(Color.green);
		g.fillRect(hsize,vsize+title,hsize,vsize);
		g.fillRect((lengthX-2)*hsize,(lengthY-2)*vsize+title,hsize,vsize);
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
			if(x==lengthX-2&&y==lengthY-2)
			{
				done=true;
				break;
			}
			int ty,tx,num;
			g.setColor(Color.red);
			if(0==parboard[x+1][y+1])
			{
				tx=x;ty=y;
				x++;y++;
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
				parboard[tx][ty]=2;
				if(x==lengthX-2&&y==lengthY-2)
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
				for(int cv=0;cv<lengthX;cv++)
				{
					for(int cv2=0;cv2<lengthY;cv2++)
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
		g.fillRect(0,title,horizbigness,vertibigness);
		g.setColor(Color.black);
	}
	//LISTENERS
	public void keyTyped(KeyEvent e)
	{
		int tx,ty;
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
		if(e.getSource()==difX||e.getSource()==difY)
		{
			e.setSource(newmaze);
		}
		Graphics g=getGraphics();
		if(e.getSource()==newmaze)
		{
			try
			{
				int tempX=lengthX;
				String s=(difX.getText()).trim();
				double d=(new Double(s.trim())).doubleValue();
				lengthX=(int)d;
				int tempY=lengthY;
				s=(difY.getText()).trim();
				d=(new Double(s.trim())).doubleValue();
				lengthY=(int)d;
				if(lengthX>4&&lengthX<251&&(!s.equals(""))||true)
				{
					hsize=horizbigness/lengthX;
					vsize=vertibigness/lengthY;
					recur=(lengthX)*(lengthY)*(lengthX+lengthY)/2;
					init();
					newMaze();
					displayMaze(g);
				}
				else
				{
					lengthX=tempX;
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
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
			g.drawLine(x*hsize+((int)(hsize/2)),y*vsize+title+((int)(vsize/2)),tx*hsize+((int)(hsize/2)),ty*vsize+((int)(vsize/2))+title);
			if(x==lengthX-2&&y==lengthY-2)
			{
				g.drawImage(end,00,50,this);
			}
		}
	}
}