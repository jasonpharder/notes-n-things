//
//  courseController.m
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-05.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "courseController.h"

extern NSString *courseName;

@implementation courseController

@synthesize courseLabel;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    courseLabel.text = @"A list of all notes belonging to this course will be displayed";
    
    self.navigationItem.title = courseName;

    
}
@end
