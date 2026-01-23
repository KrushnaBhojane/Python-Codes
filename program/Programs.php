<!DOCTYPE html>
<html>
<head>
    <title>Foliouse</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 20px;
        }
        nav {
            background-color: #333;
            text-align: center;
            padding: 10px;
        }
        nav a {
            color: white;
            text-decoration: none;
            margin: 15px;
            font-weight: bold;
        }
        nav a:hover {
            color: yellow;
        }
        .content {
            background-color: white;
            margin: 20px;
            padding: 20px;
            border-radius: 5px;
        }
        footer {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
</head>

<body>

<?php
    $websiteName = "Foliouse";
    $tagline = "Your digital creative space";
?>

<header>
    <h1><?php echo $websiteName; ?></h1>
    <p><?php echo $tagline; ?></p>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Gallery</a>
    <a href="#">Contact</a>
</nav>

<div class="content">
    <h2>About <?php echo $websiteName; ?></h2>
    <p>
        <?php
            echo "Foliouse is a creative platform that showcases designs, ideas, and digital artwork.";
        ?>
    </p>
</div>

<div class="content">
    <h2>Our Services</h2>
    <ul>
        <?php
            $services = array(
                "Creative Design",
                "Digital Art",
                "Web Templates",
                "Portfolio Creation"
            );

            foreach ($services as $service) {
                echo "<li>$service</li>";
            }
        ?>
    </ul>
</div>

<footer>
    <p>© <?php echo date("Y"); ?> Foliouse. All Rights Reserved.</p>
</footer>

</body>
</html>