rename("color");
run("Split Channels");
selectImage("color (blue)");
close();
selectImage("color (red)");
run("Green");
selectImage("color (green)");
run("Blue");
selectImage("color (red)");
run("Merge Channels...", "c2=[color (red)] c3=[color (green)] create");
