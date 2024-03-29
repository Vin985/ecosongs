<map version="freeplane 1.6.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Ecosongs" FOLDED="false" ID="ID_71652374" CREATED="1522519729749" MODIFIED="1522519873006" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <conditional_styles>
        <conditional_style ACTIVE="true" STYLE_REF="TODO" LAST="false">
            <icon_contained_condition user_name="Todo" ICON="unchecked"/>
        </conditional_style>
        <conditional_style ACTIVE="true" STYLE_REF="Done" LAST="false">
            <icon_contained_condition user_name="Done" ICON="checked"/>
        </conditional_style>
    </conditional_styles>
    <properties show_icon_for_attributes="true" fit_to_viewport="false" edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" STYLE="bubble">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
<stylenode TEXT="TODO" COLOR="#000000" BACKGROUND_COLOR="#fbe9e9" STYLE="bubble" BORDER_COLOR_LIKE_EDGE="false" BORDER_COLOR="#660000">
<font SIZE="14" BOLD="true"/>
</stylenode>
<stylenode TEXT="Done" BACKGROUND_COLOR="#99ff99" STYLE="bubble" BORDER_COLOR_LIKE_EDGE="false" BORDER_COLOR="#009900">
<font SIZE="14" BOLD="false"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#990000" BACKGROUND_COLOR="#ffcccc">
<font SIZE="16"/>
<edge COLOR="#990000"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#ff9900" BACKGROUND_COLOR="#ffffcc">
<edge COLOR="#ff9900"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#0000ff" BACKGROUND_COLOR="#ccccff">
<edge COLOR="#009900"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<node TEXT="Import files" STYLE_REF="Done" POSITION="right" ID="ID_1788271849" CREATED="1522519741879" MODIFIED="1550404561172">
<edge COLOR="#ff0000"/>
<node TEXT="convert to wav" LOCALIZED_STYLE_REF="AutomaticLayout.level,2" ID="ID_1930210986" CREATED="1522519789273" MODIFIED="1550404567252">
<node TEXT="convert to flac?" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_874684813" CREATED="1522519794338" MODIFIED="1550404573404">
<node TEXT="" ID="ID_1428265417" CREATED="1522519813970" MODIFIED="1522519813970"/>
</node>
</node>
<node TEXT="load info in database" STYLE_REF="Done" ID="ID_916902358" CREATED="1522519821744" MODIFIED="1550404578429"/>
<node TEXT="dialog widget" STYLE_REF="Done" ID="ID_533738551" CREATED="1522519852963" MODIFIED="1550404588669">
<node TEXT="Finish all options" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_426289579" CREATED="1550404593207" MODIFIED="1550404611805">
<node TEXT="Handle duplicates" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_29302424" CREATED="1550782048283" MODIFIED="1550782134593">
<node TEXT="Replace" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1043236784" CREATED="1550782061268" MODIFIED="1550782137400"/>
<node TEXT="Ignore" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_25289354" CREATED="1550782128942" MODIFIED="1550782140001"/>
</node>
</node>
</node>
</node>
<node TEXT="choose database" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" POSITION="right" ID="ID_279025532" CREATED="1522520007160" MODIFIED="1550404557364">
<node TEXT="import database" ID="ID_1888311425" CREATED="1522520542798" MODIFIED="1522520549052">
<node TEXT="import files in database" ID="ID_1973854766" CREATED="1522520550626" MODIFIED="1522520556547">
<node TEXT="conversion" ID="ID_1296112470" CREATED="1522520558348" MODIFIED="1522520563658"/>
<node TEXT="metadata" ID="ID_361405674" CREATED="1522520567117" MODIFIED="1522520573839"/>
</node>
</node>
<node TEXT="can change but only one at anytime" ID="ID_1816281800" CREATED="1522520138951" MODIFIED="1522520154477">
<node TEXT="like ENVPATH" ID="ID_1063173389" CREATED="1522520155806" MODIFIED="1522520160180"/>
</node>
</node>
<node TEXT="create project" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" POSITION="right" ID="ID_1671228807" CREATED="1522519887746" MODIFIED="1550404541579">
<node TEXT="select subset" ID="ID_1929834693" CREATED="1522520201747" MODIFIED="1522520207419">
<node TEXT="Tabs" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1582417584" CREATED="1522520222597" MODIFIED="1522520231285">
<node TEXT="one tab per subset" ID="ID_1973309631" CREATED="1522520300822" MODIFIED="1522520304482"/>
</node>
<node TEXT="analysis" ID="ID_1913043967" CREATED="1522520030189" MODIFIED="1522520258921"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      second level of tabs?
    </p>
  </body>
</html>
</richcontent>
<node TEXT="toolbar" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_261792515" CREATED="1522520049091" MODIFIED="1522520335165">
<node TEXT="one analysis per tab?" ID="ID_676382557" CREATED="1522520178050" MODIFIED="1522520194765"/>
<node TEXT="see freeplane: one map per tab, options on the toolbar on the left" ID="ID_339408957" CREATED="1522520337607" MODIFIED="1522520422500"/>
<node TEXT="one view per analysis" ID="ID_493830888" CREATED="1522520426809" MODIFIED="1522520449007"/>
</node>
<node TEXT="statistics" ID="ID_1501256027" CREATED="1522520109348" MODIFIED="1522520115070"/>
</node>
</node>
<node TEXT="save parameters" ID="ID_1257238506" CREATED="1522519910427" MODIFIED="1522519917364">
<node TEXT="subsets" ID="ID_1105917571" CREATED="1522519918249" MODIFIED="1522520044194">
<node TEXT="date" ID="ID_140773436" CREATED="1522519923713" MODIFIED="1522519925455"/>
<node TEXT="site" ID="ID_899459226" CREATED="1522519926858" MODIFIED="1522519928933"/>
<node TEXT="analysis and options" ID="ID_306660601" CREATED="1522520373006" MODIFIED="1522520379590"/>
</node>
</node>
</node>
<node TEXT="Toolbar view" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" POSITION="right" ID="ID_1709006683" CREATED="1522520463500" MODIFIED="1550404551084">
<node TEXT="Database view" ID="ID_517200063" CREATED="1522520475910" MODIFIED="1522520480632">
<node TEXT="list view" ID="ID_580267550" CREATED="1522520482826" MODIFIED="1522520487555"/>
<node TEXT="summary" ID="ID_277306006" CREATED="1522520585970" MODIFIED="1522520643266">
<node TEXT="On right" ID="ID_875136150" CREATED="1522520660335" MODIFIED="1522520665316"/>
<node TEXT="view file details" ID="ID_1070028984" CREATED="1522520666839" MODIFIED="1522520671497"/>
</node>
<node TEXT="spec view on bottom?" ID="ID_439815014" CREATED="1522520694040" MODIFIED="1522520701060"/>
</node>
<node TEXT="plot view" ID="ID_519321762" CREATED="1522520490541" MODIFIED="1522520498441">
<node TEXT="graph/image" ID="ID_882758912" CREATED="1522520500862" MODIFIED="1522520505908">
<node TEXT="spec view?" ID="ID_220978886" CREATED="1522520676404" MODIFIED="1522520681538"/>
</node>
</node>
<node TEXT="analysis view" ID="ID_342591157" CREATED="1522520511661" MODIFIED="1522520516482">
<node TEXT="text/buttons" ID="ID_1306560671" CREATED="1522520518055" MODIFIED="1522520523111"/>
</node>
</node>
<node TEXT="AudioManager" POSITION="left" ID="ID_763832084" CREATED="1550404049491" MODIFIED="1550404055580">
<node TEXT="File tree view" STYLE_REF="Done" ID="ID_861506097" CREATED="1534108210971" MODIFIED="1550404447026">
<node TEXT="Delete recording" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1462938834" CREATED="1550782030943" MODIFIED="1550782038416">
<node TEXT="delete all related information" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_634488262" CREATED="1551885847066" MODIFIED="1551885892043"/>
<node TEXT="update tree view" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_684939027" CREATED="1551885858411" MODIFIED="1551885894788">
<node TEXT="Delete all parents if no more child" ID="ID_1192881045" CREATED="1551899214708" MODIFIED="1551899224899"/>
</node>
<node TEXT="Change text based on selected information" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1818669027" CREATED="1551885903628" MODIFIED="1551885917235"/>
</node>
</node>
<node TEXT="Analysis" STYLE_REF="Done" ID="ID_1751091927" CREATED="1550404067355" MODIFIED="1550404453299">
<node TEXT="Indexes" STYLE_REF="Done" ID="ID_992375452" CREATED="1550404073185" MODIFIED="1550404456347">
<node TEXT="ACI" STYLE_REF="Done" ID="ID_91128739" CREATED="1550404078193" MODIFIED="1550404465395"/>
</node>
<node TEXT="Song detection" STYLE_REF="Done" ID="ID_56802018" CREATED="1550404083565" MODIFIED="1551454864867">
<node TEXT="Overwrite results" STYLE_REF="Done" ID="ID_481332997" CREATED="1550404290161" MODIFIED="1551454864866"/>
<node TEXT="Save detection options" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_706731544" CREATED="1551454867635" MODIFIED="1551454879802"/>
<node TEXT="Benchmark options" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_503146154" CREATED="1551454891490" MODIFIED="1551885938147"/>
<node TEXT="Allow for multiple detections" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_97169668" CREATED="1551890179451" MODIFIED="1551890201023">
<node TEXT="Add multiple process options" ID="ID_1121109467" CREATED="1552331948701" MODIFIED="1552331962426"/>
</node>
</node>
</node>
<node TEXT="GUI" ID="ID_1614658667" CREATED="1550404242986" MODIFIED="1550404244564">
<node TEXT="Contextual Dialog" STYLE_REF="Done" ID="ID_1576334714" CREATED="1550404245720" MODIFIED="1550404505821">
<node TEXT="AnalyserDialog" STYLE_REF="Done" ID="ID_256961476" CREATED="1550404258088" MODIFIED="1550404500244">
<node TEXT="Save settings" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1352675262" CREATED="1550404280253" MODIFIED="1550404406368"/>
<node TEXT="Create parent widget" LOCALIZED_STYLE_REF="AutomaticLayout.level,2" ID="ID_627361703" CREATED="1550404311453" MODIFIED="1550404426154"/>
<node TEXT="Do not perform analysis if already exists" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1414402158" CREATED="1550781993783" MODIFIED="1550782019599"/>
<node TEXT="Add help tooltips" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_1295589993" CREATED="1551454796268" MODIFIED="1551885927830"/>
</node>
</node>
<node TEXT="Tree view" ID="ID_443503103" CREATED="1551885871310" MODIFIED="1551885874456">
<node TEXT="Speed up tree loading" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1126319422" CREATED="1551885875486" MODIFIED="1551885887422"/>
</node>
</node>
<node TEXT="Details" ID="ID_1158438779" CREATED="1551893778711" MODIFIED="1551893785499">
<node TEXT="Update details when selecting more than one recording" ID="ID_1437638346" CREATED="1551893787067" MODIFIED="1551893808477"/>
</node>
</node>
<node TEXT="Database management" POSITION="left" ID="ID_390417758" CREATED="1551455309238" MODIFIED="1551455401417">
<node TEXT="Create dict of models in main app" STYLE_REF="Done" ID="ID_1632665224" CREATED="1551455319943" MODIFIED="1551885956381">
<node TEXT="load at startup" ID="ID_1901760926" CREATED="1551455331607" MODIFIED="1551455335580"/>
<node TEXT="Where to list all models?" ID="ID_952640881" CREATED="1551455611618" MODIFIED="1551455618449"/>
</node>
<node TEXT="Have one item always loaded in memory" ID="ID_1590380273" CREATED="1551455353346" MODIFIED="1551455401415">
<node TEXT="Add" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_769053315" CREATED="1551455373955" MODIFIED="1551455415013"/>
<node TEXT="Delete" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1554719227" CREATED="1551455385025" MODIFIED="1551455419110"/>
<node TEXT="Update" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" ID="ID_1965449311" CREATED="1551455388602" MODIFIED="1551455422515"/>
</node>
</node>
</node>
</map>
