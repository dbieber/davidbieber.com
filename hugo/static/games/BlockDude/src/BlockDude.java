import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
/**
 *BlockDude -By David Bieber
 */
public class BlockDude extends JApplet implements KeyListener, ActionListener
{
      private static final long serialVersionUID = 1L;

      LevelMaker level,player;
      boolean levelSet,firstTime=true,isPlaying=true;
      int levelNumber=1,numOfLevels=11;
      String mode="original",imageStyle="calc";
      Image offscreen;
      Graphics g;
      Image BlockDudeLeft,BlockDudeRight,Block,Brick,Nothing,Door,MenuImage;
      BlockDudeLevel currentLevel;
      Toolkit toolkit=Toolkit.getDefaultToolkit();
      Dimension dim;
      public void init()
      {
         getContentPane().setLayout(null);
         dim = getSize();
         offscreen = createImage(dim.width,dim.height);
         g = offscreen.getGraphics();
         levelSet=true;
         JMenuBar menuBar;
         JMenu file,menu1, menu2,menu3;
         JMenuItem menuItem;
         JRadioButtonMenuItem rbMenuItem;
         menuBar = new JMenuBar();
         file = new JMenu("Level");
         menuItem=new JMenuItem("Restart");
         file.add(menuItem);
         menuItem.addActionListener(this);
         menuItem=new JMenuItem("Next");
         file.add(menuItem);
         menuItem.addActionListener(this);
         menuItem=new JMenuItem("Previous");
         file.add(menuItem);
         menuItem.addActionListener(this);
         menuBar.add(file);
         menu1 = new JMenu("Graphics");
         menuBar.add(menu1);
         ButtonGroup group = new ButtonGroup();
         rbMenuItem = new JRadioButtonMenuItem("Calculator");
         rbMenuItem.setSelected(true);
         rbMenuItem.addActionListener(this);
         group.add(rbMenuItem);
         menu1.add(rbMenuItem);
         rbMenuItem = new JRadioButtonMenuItem("Color");
         rbMenuItem.addActionListener(this);
         group.add(rbMenuItem);
         menu1.add(rbMenuItem);
         rbMenuItem = new JRadioButtonMenuItem("Text");
         rbMenuItem.addActionListener(this);
         group.add(rbMenuItem);
         menu1.add(rbMenuItem);
         rbMenuItem = new JRadioButtonMenuItem("3D");
         rbMenuItem.addActionListener(this);
         group.add(rbMenuItem);
         menu1.add(rbMenuItem);
         menu1.addSeparator();
         rbMenuItem = new JRadioButtonMenuItem("Custom Graphics");
         rbMenuItem.addActionListener(this);
         group.add(rbMenuItem);
         menu1.add(rbMenuItem);
         menu2 = new JMenu("Difficulty");menuBar.add(menu2);
         menuBar.add(menu1);
         ButtonGroup group2 = new ButtonGroup();
         rbMenuItem = new JRadioButtonMenuItem("Original");
         rbMenuItem.setSelected(true);
         rbMenuItem.addActionListener(this);
         group2.add(rbMenuItem);
         menu2.add(rbMenuItem);
         menu2.addSeparator();
         rbMenuItem = new JRadioButtonMenuItem("Beginner");
         rbMenuItem.addActionListener(this);
         group2.add(rbMenuItem);
         menu2.add(rbMenuItem);
         rbMenuItem = new JRadioButtonMenuItem("Intermediate");
         rbMenuItem.addActionListener(this);
         group2.add(rbMenuItem);
         menu2.add(rbMenuItem);
         rbMenuItem = new JRadioButtonMenuItem("Advanced");
         rbMenuItem.addActionListener(this);
         group2.add(rbMenuItem);
         menu2.add(rbMenuItem);
         rbMenuItem = new JRadioButtonMenuItem("Expert");
         rbMenuItem.addActionListener(this);
         group2.add(rbMenuItem);
         menu2.add(rbMenuItem);
         rbMenuItem = new JRadioButtonMenuItem("Other");
         rbMenuItem.addActionListener(this);
         group2.add(rbMenuItem);
         menu2.add(rbMenuItem);
         menu2.addSeparator();
         rbMenuItem = new JRadioButtonMenuItem("Custom Level");
         rbMenuItem.addActionListener(this);
         group2.add(rbMenuItem);
         menu2.add(rbMenuItem);
         menu3=new JMenu("HELP");
         menuItem=new JMenuItem("Information");
         menuItem.addActionListener(this);
         menu3.add(menuItem);
         menuItem=new JMenuItem("Instructions");
         menuItem.addActionListener(this);
         menu3.add(menuItem);
         menuBar.add(menu3);
         this.setJMenuBar(menuBar);
         this.setVisible(true);
         addKeyListener(this);
         JRootPane rootPane=this.getRootPane();
         rootPane.putClientProperty("defeatSystemEventQueueCheck", Boolean.TRUE);
         Nothing=getImage(getDocumentBase(),"images/Space"+imageStyle+".GIF");
         BlockDudeLeft=getImage(getDocumentBase(),"images/BlockDudeLeft"+imageStyle+".GIF");
         BlockDudeRight=getImage(getDocumentBase(),"images/BlockDudeRight"+imageStyle+".GIF");
         Block=getImage(getDocumentBase(),"images/Block"+imageStyle+".GIF");
         Brick=getImage(getDocumentBase(),"images/Brick"+imageStyle+".GIF");
         Door=getImage(getDocumentBase(),"images/Door"+imageStyle+".GIF");
         MenuImage=getImage(getDocumentBase(),"images/Menu.JPG");
         repaint();
      }
      public void repaint()
      {
         isPlaying=false;
         paint(getGraphics());
         isPlaying=true;
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
      public String getImageStyle()
      {
         return imageStyle;
      }
      public void setImageStyle(String is)
      {
         imageStyle=is;
         Nothing=getImage(getDocumentBase(),"images/Space"+imageStyle+".GIF");
         BlockDudeLeft=getImage(getDocumentBase(),"images/BlockDudeLeft"+imageStyle+".GIF");
         BlockDudeRight=getImage(getDocumentBase(),"images/BlockDudeRight"+imageStyle+".GIF");
         Block=getImage(getDocumentBase(),"images/Block"+imageStyle+".GIF");
         Brick=getImage(getDocumentBase(),"images/Brick"+imageStyle+".GIF");
         Door=getImage(getDocumentBase(),"images/Door"+imageStyle+".GIF");
         currentLevel.display();
         
      }
      public void update(Graphics gr)
      {
         paint(gr);
      }
      public void setMode(String m)
      {
         mode=m;
         levelNumber=1;
         if(m.equals("original"))
         {
            numOfLevels=11;
         }
         else if(m.equals("beginner"))
         {
            numOfLevels=7;
         }
         else if(m.equals("intermediate"))
         {
            numOfLevels=0;
         }
         else if(m.equals("advanced"))
         {
            numOfLevels=0;
         }
         else if(m.equals("expert"))
         {
            numOfLevels=1;
         }
         else if(m.equals("other"))
         {
            numOfLevels=4;
         }
         else
            numOfLevels=1;
         repaint();
      }
      public String getMode()
      {
         return mode;
      }
      public void start()
      {
         //prompt menu options
      }
      public void stop()
      {
         //save to backup here
      }
      public void paint(Graphics gr)
      {
         g.drawImage(MenuImage,0,0,this);
         g.setColor(Color.white);
         g.fillRect(-10,24,780,780);
         if(!isPlaying)
         {
            if(levelNumber<=numOfLevels)
               level=new LevelMaker(mode+levelNumber+".level");
            else
               level=new LevelMaker("WIN.level");
            currentLevel=new BlockDudeLevel(level,this);
         }
         currentLevel.display();
         gr.drawImage(offscreen,0,0,this);
      }
      public void levelUp()
      {
         levelNumber++;
         repaint();
      }
      public String getAppletInfo()
      {
         return "Title: BlockDude\n"+"Author: David Bieber\n"+"Based on the TI-83+ Calculator Game.";
      }
      public void keyTyped(KeyEvent e)
      {
         if(e.getKeyChar()=='a')
         {
            currentLevel.left();
            repaint();//currentLevel.display();
         }
         if(e.getKeyChar()=='d')
         {
            currentLevel.right();
            repaint();//currentLevel.display();
         }
         if(e.getKeyChar()=='w')
         {
            currentLevel.up();
            repaint();//currentLevel.display();
         }
         if(e.getKeyChar()=='s')
         {
            currentLevel.liftOrDrop();
            repaint();//currentLevel.display();
         }
      }
      public void keyPressed(KeyEvent e)
      {
         if(e.getKeyCode()==37)
         {
            currentLevel.left();
            repaint();//currentLevel.display();
         }
         if(e.getKeyCode()==39)
         {
            currentLevel.right();
            repaint();//currentLevel.display();
         }
         if(e.getKeyCode()==38)
         {
            currentLevel.up();
            repaint();//currentLevel.display();
         }
         if(e.getKeyCode()==40)
         {
            currentLevel.liftOrDrop();
            repaint();//currentLevel.display();
         }
      }
      public void keyReleased(KeyEvent e){}
      public void actionPerformed(ActionEvent e)
      {
         Graphics g=getGraphics();
         g.setColor(Color.white);
         g.fillRect(-1,24,1100,1000);
         if(e.getActionCommand().equals("Text"))
         {
            setImageStyle("Text");
         }
         if(e.getActionCommand().equals("Calculator"))
         {
            setImageStyle("Calc");
         }
         if(e.getActionCommand().equals("Color"))
         {
            setImageStyle("Color");
         }
         if(e.getActionCommand().equals("3D"))
         {
            setImageStyle("3D");
         }
         if(e.getActionCommand().equals("Original"))
         {
            setMode("original");
         }
         if(e.getActionCommand().equals("Beginner"))
         {
            setMode("beginner");
         }
         if(e.getActionCommand().equals("Intermediate"))
         {
            setMode("intermediate");
         }
         if(e.getActionCommand().equals("Advanced"))
         {
            setMode("advanced");
         }
         if(e.getActionCommand().equals("Expert"))
         {
            setMode("expert");
         }
         if(e.getActionCommand().equals("Other"))
         {
            setMode("other");
         }
         if(e.getActionCommand().equals("Instructions"))
         {
            JOptionPane.showMessageDialog(null,"BlockDude. A puzzle game. Use the arrow keys to move and pick up blocks.",
                                          "Instructions",JOptionPane.INFORMATION_MESSAGE);
         }
         if(e.getActionCommand().equals("Information"))
         {
            JOptionPane.showMessageDialog(null,"UNDER CONSTRUCTION","Information",JOptionPane.INFORMATION_MESSAGE);
         }
         if(e.getActionCommand().equals("Next"))
         {
            levelUp();
         }
         if(e.getActionCommand().equals("Previous"))
         {
            if(levelNumber!=1)
            {
               levelNumber--;
               
            }
            if(levelNumber>numOfLevels)
            {
               levelNumber=numOfLevels;
            }
            repaint();
         }
         if(e.getActionCommand().equals("Restart"))
         {
            repaint();
         }
         currentLevel.display();
      }
}