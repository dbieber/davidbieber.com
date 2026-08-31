import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
import java.io.*;
public class BlockDudeLevelEditor extends JApplet implements MouseListener, ActionListener
{
    String[][] level;
    boolean isEditing,isPlaying;
    TextArea fileName;
    Button newFile,openFile,getCode;
    Image Nothing,Block,Brick,BlockDudeLeft,BlockDudeRight,Door;
    ImageIcon nothing,block,brick,blockDudeLeft,blockDudeRight,door;
    String imageStyle="Calc";
    JButton space,bl,br,bdl,bdr,d;
    String file;
    String currentTool;
    int maxX=-1,maxY=-1,minX=46,minY=26,playerX=-1,playerY=-1;
    public void init()
    {
        level=new String[45][25];
        maxX=-1;
        maxY=-1;
        minX=46;
        minY=26;
        playerX=-1;
        playerY=-1;
        addMouseListener(this);
        isEditing=false;
        JRootPane rootPane = this.getRootPane();    
        rootPane.putClientProperty("defeatSystemEventQueueCheck", Boolean.TRUE);
        currentTool=" ";
        getContentPane().setLayout(null);
        fileName=new TextArea("*.level");
        newFile=new Button("NEW");
        openFile=new Button("OPEN");
        getCode=new Button("GET CODE");
        Nothing=getImage(getDocumentBase(),"images/Space"+imageStyle+".GIF");
        BlockDudeLeft=getImage(getDocumentBase(),"images/BlockDudeLeft"+imageStyle+".GIF");
        BlockDudeRight=getImage(getDocumentBase(),"images/BlockDudeRight"+imageStyle+".GIF");
        Block=getImage(getDocumentBase(),"images/Block"+imageStyle+".GIF");
        Brick=getImage(getDocumentBase(),"images/Brick"+imageStyle+".GIF");
        Door=getImage(getDocumentBase(),"images/Door"+imageStyle+".GIF");
        nothing=new ImageIcon(Nothing);
        blockDudeLeft=new ImageIcon(BlockDudeLeft);
        blockDudeRight=new ImageIcon(BlockDudeRight);
        block=new ImageIcon(Block);
        brick=new ImageIcon(Brick);
        door=new ImageIcon(Door);
        space=new JButton(nothing);
        bl=new JButton(block);
        br=new JButton(brick);
        bdl=new JButton(blockDudeLeft);
        bdr=new JButton(blockDudeRight);
        d=new JButton(door);
        newFile.setBounds(9,10,41,20);
        openFile.setBounds(55,10,46,20);
        getCode.setBounds(106,10,75,20);
        fileName.setBounds(185,10,908,52);
        space.setBounds(10,35,24,24);
        d.setBounds(39,35,24,24);
        bdl.setBounds(68,35,24,24);
        bdr.setBounds(97,35,24,24);
        br.setBounds(126,35,24,24);
        bl.setBounds(155,35,24,24);
        d.addActionListener(this);
        bdl.addActionListener(this);
        bdr.addActionListener(this);
        bl.addActionListener(this);
        br.addActionListener(this);
        space.addActionListener(this);
        newFile.addActionListener(this);
        openFile.addActionListener(this);
        getCode.addActionListener(this);
        getContentPane().add(newFile);
        getContentPane().add(openFile);
        getContentPane().add(getCode);
        getContentPane().add(fileName);
        getContentPane().add(d);
        getContentPane().add(bl);
        getContentPane().add(br);
        getContentPane().add(bdl);
        getContentPane().add(bdr);
        getContentPane().add(space);
    }
    public void start()
    {
        newLevel();
    }
    public void stop()
    {
    }
    public void paint(Graphics g)
    {
        g.setColor(Color.white);
        g.fillRect(-1,-1,2000,2000);
        g.setColor(Color.black);
        g.fillRect(9,34,171,26);
        g.setColor(new Color(60,60,60));
        g.drawString("Move your mouse here",33,50);
        if(isEditing)
        {
            for(int cv=minX;cv<=maxX;cv++)
            {
                for(int cv2=minY;cv2<=maxY;cv2++)
                {  
                    g.drawImage(getImage(level[cv][cv2]),24*cv+10,24*cv2+64,this);
                }
            }
        }
    }
    public void destroy()
    {
    }
    public String getAppletInfo()
    {
        return "Title: BlockDude-Level Editor \nAuthor: David Bieber \nAllows the user to create or edit a BlockDudeLevel";
    }
    public void mouseExited(MouseEvent e){}
    public void mouseEntered(MouseEvent e){}
    public void mouseReleased(MouseEvent e){}
    public void mouseClicked(MouseEvent e){}
    public void mousePressed(MouseEvent e)
    {
        if(isEditing)
        {
            int mx=e.getX()-10;
            int my=e.getY()-64;
            int x=(int)(mx/24);
            int y=(int)(my/24);
            if(x>44||y>24||x<0||y<0)
            return;
            if(currentTool.equals("L")||currentTool.equals("R"))
            {
                if(playerX!=-1&&playerY!=-1)
                {
                    level[playerX][playerY]=" ";
                    getGraphics().drawImage(getImage(" "),24*playerX+10,24*playerY+64,this);
                }
                playerX=x;
                playerY=y;
            }
            getGraphics().drawImage(getImage(currentTool),24*x+10,24*y+64,this);
            level[x][y]=currentTool;
                limitBorders(x,y);
            if(!currentTool.equals(" "))
            {
                if(x<minX)
                minX=x;
                if(x>maxX)
                maxX=x;
                if(y<minY)
                minY=y;
                if(y>maxY)
                maxY=y;
            }
        }
    }
    public void actionPerformed(ActionEvent e)
    {
    	if(e.getSource()==fileName)
    	{
    		if(isPlaying)
    		{
    			isPlaying=false;
    			//return;
    		}
    		else
    		{
    			isPlaying=true;
    		}
    	}
        if(e.getSource()==space)
        {
            setTool(" ");
        }
        if(e.getSource()==br)
        {
            setTool("x");
        }
        if(e.getSource()==bl)
        {
            setTool("o");
        }
        if(e.getSource()==d)
        {
            setTool("G");
        }
        if(e.getSource()==bdl)
        {
            setTool("L");
        }
        if(e.getSource()==bdr)
        {
            setTool("R");
        }
        if(e.getSource()==newFile)
        {
            newLevel();
        }
        if(e.getSource()==openFile)
        {
            openLevel();
        }
        if(e.getSource()==getCode)
        {
        	getCode();
        }
    }
    public void setTool(String tool)
    {
        currentTool=tool;
    }
    public Image getImage(String i)
    {
        if(i.equals(" "))
        {
            return Nothing;
        }
        if(i.equals("L"))
        {
            return BlockDudeLeft;
        }
        if(i.equals("R"))
        {
            return BlockDudeRight;
        }
        if(i.equals("G"))
        {
            return Door;
        }
        if(i.equals("x"))
        {
            return Brick;
        }
        if(i.equals("o"))
        {
            return Block;
        }
        return Nothing;
    }
    public void newLevel()
    {
        maxX=-1;
        maxY=-1;
        minX=46;
        minY=26;
        level=new String[45][25];
        for(int cv=0;cv<45;cv++)
        {
            for(int cv2=0;cv2<25;cv2++)
            {
                level[cv][cv2]=" ";
            }
        }
        isEditing=true;
        repaint();
    }
    public void openLevel()
    {
        file=fileName.getText();
        if(file.equals("*.level")||!file.substring(file.length()-6).equals(".level")||file.length()<7)
        {
            fileName.setText("You must specify a valid '.level' file.");
            file=null;
            return;
        }
        LevelMaker in=new LevelMaker(file);
        if(in.bad())
        {
            fileName.setText("The file specified is either missing or corupt.");
            file=null;
            return;
        }
		String line;
        maxX=in.readInt()-1;
        minX=0;
        maxY=in.readInt()-1;
        minY=0;
		for(int xa=0;xa<45;xa++)
		{
			for(int ya=0;ya<25;ya++)
			{
				level[xa][ya]=" ";
			}
		}
		int cvy=0;
        while(cvy<=maxY)
        {
            line=in.readLine();
            int cvx=0;
            while(cvx<line.length())
            {
                level[cvx][cvy]=line.substring(cvx,cvx+1);
                if(level[cvx][cvy].equals("L")||level[cvx][cvy].equals("R"))
                {
                    playerX=cvx;
                    playerY=cvy;
                }
                cvx++;
            }
            cvy++;
        }
        isEditing=true;
        repaint();
        repaint();
    }
    public void saveLevel()
    {
        file=fileName.getText();
        if(file.equals("*.level")||!file.substring(file.length()-6).equals(".level")||file.length()<7)
        {
            fileName.setText("You must specify a valid '.level' file.");
            file=null;
            return;
        }
        if(file.substring(0,8).equals("original")||file.substring(0,8).equals("beginner")||file.substring(0,12).equals("intermediate")||file.substring(0,8).equals("advanced")||file.substring(0,8).equals("expert")||file.substring(0,5).equals("other")||file.equals("WIN.level"))
        {
            fileName.setText("The file name you specified has is reserved.");
            file=null;
            return;
        }
        PrintWriter out=null;
        try
        {
            File DATA_OUT=new File("levels/"+file);
            out = new PrintWriter(new OutputStreamWriter(new FileOutputStream(DATA_OUT)));
        }
        catch(IOException ioe)
        {
            fileName.setText("An error has occured."+ioe);
            file=null;
            return;
        }
        String line1=maxX-minX+"";
        String line2=maxX-minX+"";
        String line3="";
        for(int cv=minY;cv<=maxY;cv++)
        {
            for(int cv2=minX;cv2<=maxX;cv2++)
            {
                line3+=level[cv2][cv];
            }   
            line3+="\n";
        }
        out.println(line1);
        out.println(line2);
        out.print(line3);
        out.close();
    }
    public void limitBorders(int x,int y)
    {
        maxX=-1;maxY=-1;minX=46;minY=26;
        for(int cv=0;cv<45;cv++)
        {
        	for(int cv2=0;cv2<25;cv2++)
        	{
        		if(!level[cv][cv2].equals(" "))
        		{
        			if(cv<minX)
        			{
        				minX=cv;
        			}
        			if(cv>maxX)
        			{
        				maxX=cv;
        			}
        			if(cv2<minY)
        			{
        				minY=cv2;
        			}
        			if(cv2>maxY)
        			{
        				maxY=cv2;
        			}
        		}
        	}
        }
        repaint();
    }
    public void getCode()
    {
    	String code=   "		else if(levelName.equals("+'"'+"other.level"+'"'+"))\n";
    			code+= "		{\n";
				code+= "			num1="+(maxX-minX+1)+";\n";
				code+= "			num2="+(maxY-minY+1)+";\n";
				code+= "			lines=new String[num2];\n";
        for(int cv=minY;cv<=maxY;cv++)
        {
            code+="			lines["+(cv-minY)+"]="+'"';
            for(int cv2=minX;cv2<=maxX;cv2++)
            {
                code+=level[cv2][cv];
            }
            code+='"'+";\n";
        }
    	code+= "		}";
        fileName.setText(code);
    }
}