self.mouth.undraw()
        theta=start_angle
        while(theta < end_angle):
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = math.cos(theta) * radius + center_point.getY()
            point1 = Point(x_coord, y_coord)
            point1.draw(window)
            theta+=0.03