<?

function insert_category_header($category){
	 switch ($category) {
	 	case "americanartists":
  		     echo "<span class=\"clHeaderportf\">AMERICAN ARTISTS 1975 - 1989</span><br /><br />"
		         ."<strong>Limited Editions 1971 - 2003<br /><br />"
			 ."  VIDEO PORTRAITS FOR INSTALLATIONS</strong><br /><br />";
 		     break;
		case "firstvideo":
  		     echo "<span class=\"clHeaderportf\">FIRST VIDEO PORTRAIT 1971</span><br /><br />"
		         ."<strong>West Africa: Outside Looking In<br><br>"
			 ."VIDEO PORTRAITS FOR INSTALLATIONS</strong><br /><br />";
  		     break;
		case "civilrights":
  		     echo "<span class=\"clHeaderportf\">CIVIL RIGHTS PIONEERS</span><br /><br />";
  		     break;
		case "frenchartists":
  		     echo "<span class=\"clHeaderportf\">FRENCH ARTISTS 1982-1983</span><br /><br />"
		         ."<strong>30 Second Portraits<br /><br />"
			 ."  VIDEO PORTRAITS FOR INSTALLATIONS</strong><br /><br />";
  		     break;
	}
}

function insert_thumbnails($category){
     echo "<table border=\"0\" cellspacing=\"8\">";
     echo "<tr>";     
     $path = "categoriesTXT/".$category.".txt";
     $handle = fopen($path, "r");
     $row_index=0;
     if ($handle) {
          while (!feof($handle)) {
              $buffer = fgets($handle, 4096);
              $fields = split(',',$buffer);
              $title = ereg_replace('"', '', $fields[0]);
              $location = ereg_replace('"', '', $fields[1]);
              $video = ereg_replace('"', '', $fields[2]);
              $thumbnail = ereg_replace('"', '', $fields[3]);
              if(strlen($title) > 3){
                  $row_index++;
		  echo "<td><a href=\"level3.php?category=$category&videosrc=$video\"\"><img src=\"thumbnails/$category/$thumbnail\"></a></td>";
		  if($row_index > 3){
		  	echo "</tr>\n<tr>";
			$row_index=0;			
		  }
              }
          }
     }
     echo "</tr>";
     echo "</table>";
}

function l1_output_category($categoryname){
     $path = "categoriesTXT/".$categoryname.".txt";
     $handle = fopen($path, "r");
     if ($handle) {
     while (!feof($handle)) {
     $buffer = fgets($handle, 4096);
          $fields = split(',',$buffer);
          $title = ereg_replace('"', '', $fields[0]);
          $location = ereg_replace('"', '', $fields[1]);
          $video = ereg_replace('"', '', $fields[2]);
          $thumbnail = ereg_replace('"', '', $fields[3]);
          if(strlen($title) > 3){
               echo "<a href=\"level3.php?category=$categoryname&videosrc=$video\">".$title." <span class=\"stylesm\">".$location."</a></span><br /> ";
            }
     }
     fclose($handle);
     }
     
}


?>