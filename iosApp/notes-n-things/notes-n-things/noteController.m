//
//  noteController.m
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-05.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "noteController.h"

@implementation noteController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    self.navigationItem.title = @"title";
    noteLabel.text = @"hello";
}
@end
