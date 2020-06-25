<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>my car favorite</title>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.js"></script>
    <style type="text/css">
        .wrapper{
            width: 650px;
            margin: 0 auto;
        }
        .page-header h2{
            margin-top: 0;
        }
        table tr td:last-child a{
            margin-right: 15px;
        }
    </style>
    <script type="text/javascript">
        $(document).ready(function(){
            $('[data-toggle="tooltip"]').tooltip();   
        });
    </script>
</head>
<body>
    <div class="wrapper" style="background-color: rgba(123,111,23,0.2);">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="page-header clearfix">
                        <h2 class="pull-left">Car Details</h2>
                        <a href="create.php" class="btn btn-success pull-right">add new Car</a>
                    </div>
                    <?php 
                        require_once "config.php";
                        
                        $sql = "SELECT * FROM car";
                        if($result = $mysqli->query($sql)){
                            if ($result -> num_rows>0) {
                                echo "<table class='table table-bordered table-striped'";
                                echo "<thead>";
                                echo "<tr>";
                                echo "<th>PLACA</th>";
                                echo "<th>MARCA</th>";
                                echo "<th>MODELO</th>";
                                echo "<th>COLOR</th>";
                                echo "<th>AÑO</th>";
                                echo "<th>action</th>";
                                echo "</tr>";
                                echo "</thead>";
                                echo "<tbody>";
                                while($row = $result->fetch_array()){
                                    echo "<br>";
                                        echo "<td>" . $row['id_placa']. "</td>";
                                        echo "<td>" . $row['marca']. "</td>";
                                        echo "<td>" . $row['modelo']. "</td>";
                                        echo "<td>" . $row['color']. "</td>";
                                        echo "<td>" . $row['year_']. "</td>";
                                        echo "<td>";
                                        
                                        echo "<a href='read.php?id=". $row['id_placa'] ."' title='View Record' data-toggle='tooltip'><span class='glyphicon glyphicon-eye-open'></span></a>";
                                            echo "<a href='update.php?id=". $row['id_placa'] ."' title='Update Record' data-toggle='tooltip'><span class='glyphicon glyphicon-pencil'></span></a>";
                                            echo "<a href='delete.php?id=". $row['id_placa'] ."' title='Delete Record' data-toggle='tooltip'><span class='glyphicon glyphicon-trash'></span></a>";
                                        echo "</td>";
                                    echo "</tr>";
                                }
                                echo "</tbody>";                            
                            echo "</table>";
                            // Free result set
                            $result->free();
                        } else{
                            echo "<p class='lead'><em>No records were found.</em></p>";
                        }
                    } else{
                        echo "ERROR: Could not able to execute $sql. " . $mysqli->error;
                    }
                    
                    // Close connection
                    $mysqli->close();
                    ?>
                </div>
            </div>        
        </div>
    </div>
</body>
</html>