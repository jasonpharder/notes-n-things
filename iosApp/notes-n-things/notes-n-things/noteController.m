//
//  noteController.m
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-05.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "noteController.h"

extern NSString *noteTitle;

@implementation noteController

@synthesize noteLabel;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    self.navigationItem.title = noteTitle;

    noteLabel.text = @"Where the note context will be displayed";
}
@end
